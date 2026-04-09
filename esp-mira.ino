#include <Adafruit_NeoPixel.h>
#include <string.h>

#define LED_PIN    15
#define TOUCH_PIN  14

#define TOUCH_THRESHOLD  210

#define OUTER_RING 24    
#define INNER_RING 16    
#define NUM_LEDS   (OUTER_RING + INNER_RING) 

Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

// Binary protocol constants
static const uint8_t PROTO_SOF = 0x7E;
static const uint8_t BIN_CMD_SET_ONE   = 0x11;
static const uint8_t BIN_CMD_SET_BLOCK = 0x12;
static const uint8_t BIN_CMD_SET_ALL   = 0x13;
static const uint8_t BIN_CMD_APPLY     = 0x14;
static const uint8_t BIN_CMD_TOUCH_THR = 0x15;
static const uint8_t GROUP_OUTER = 0;
static const uint8_t GROUP_INNER = 1;
static const uint8_t APPLY_ENABLE_PIXEL  = 0;
static const uint8_t APPLY_DISABLE_PIXEL = 1;
static const uint8_t BIN_EVT_TOUCH = 0x81;
static const uint8_t BIN_ACK       = 0xF0;
static const uint8_t BIN_ERR       = 0xF1;
static const uint8_t TOUCH_EVT_PRESS   = 1;
static const uint8_t TOUCH_EVT_RELEASE = 2;
static const uint8_t TOUCH_EVT_HOLD    = 3;
static const uint8_t ERR_BAD_LEN     = 1;
static const uint8_t ERR_BAD_INDEX   = 2;
static const uint8_t ERR_BAD_COUNT   = 3;
static const uint8_t ERR_BAD_MODE    = 4;
static const uint8_t ERR_BAD_CMD     = 5;
static const uint8_t ERR_BAD_CHECK   = 6;

struct LedPixel {
  uint8_t r;
  uint8_t g;
  uint8_t b;
  uint8_t bri;
};

struct BinParser {
  uint8_t state;
  uint8_t cmd;
  uint8_t seq;
  uint8_t len;
  uint8_t idx;
  uint8_t chk;
  uint8_t payload[200];
};

HardwareSerial SerialData(2);

uint16_t g_touchThr = TOUCH_THRESHOLD;
LedPixel g_ledStage[NUM_LEDS];
LedPixel g_ledActive[NUM_LEDS];
bool     g_ledDirty = true;

BinParser g_binParserU2  = {0};
BinParser g_binParserUSB = {0};
Stream*   g_respStream = &SerialData;

void processSerialDataInput();
void processBinaryByte(BinParser& p, uint8_t b);
void handleBinaryFrame(uint8_t cmd, uint8_t seq, uint8_t len, uint8_t* payload);
int  mapGroupIndexToLed(int group, int idx);
void copyStageToActive();
void clearActiveLeds();
void renderActiveLeds();
void sendBinaryFrame(uint8_t cmd, uint8_t seq, uint8_t len, const uint8_t* payload);
void sendBinOk(uint8_t reqCmd, uint8_t seq);
void sendBinErr(uint8_t reqCmd, uint8_t seq, uint8_t errCode);
void sendTouchEvent(uint8_t type, uint16_t raw);
void processDebugText(const char* line);

volatile bool     g_touchIRQ    = false;
static void IRAM_ATTR onTouchISR(void* arg) {
  g_touchIRQ = true;
  (void)arg;
}

void setup() {
  Serial.begin(115200);
  SerialData.begin(115200, SERIAL_8N1, 16, 17);
  strip.begin();
  strip.setBrightness(255);
  strip.show();
  for (int i = 0; i < NUM_LEDS; i++) {
    g_ledStage[i] = {0, 0, 0, 0};
    g_ledActive[i] = {0, 0, 0, 0};
  }
  touchAttachInterruptArg(TOUCH_PIN, onTouchISR, nullptr, g_touchThr);
  renderActiveLeds();
  const char* readyMsg = "Ready. Binary protocol active (UART2 + USB Serial).\r\n";
  Serial.print(readyMsg);
  Serial.println("USB Serial debug commands:");
  Serial.println("  ALL,R,G,B,BRI   - set all 40 LEDs and apply");
  Serial.println("  ONE,grp,idx,R,G,B,BRI - set one LED and apply");
  Serial.println("  BRI,val         - set all LEDs brightness");
  Serial.println("  OFF             - turn off all LEDs");
  Serial.println("  THR,val         - set touch threshold");
  Serial.println("  HELP            - show this help");
  SerialData.print(readyMsg);
}

void loop() {
  processSerialDataInput();
  static bool lastTouched = false;
  static unsigned long lastHoldReport = 0;

  uint16_t touchVal = (uint16_t)touchRead(TOUCH_PIN);
  bool isTouched = (touchVal < g_touchThr) || g_touchIRQ;
  g_touchIRQ = false;

  if (isTouched && !lastTouched) sendTouchEvent(TOUCH_EVT_PRESS, touchVal);
  if (!isTouched && lastTouched) sendTouchEvent(TOUCH_EVT_RELEASE, touchVal);
  if (isTouched && millis() - lastHoldReport >= 500) {
    lastHoldReport = millis();
    sendTouchEvent(TOUCH_EVT_HOLD, touchVal);
  }
  lastTouched = isTouched;

  if (g_ledDirty) {
    renderActiveLeds();
    g_ledDirty = false;
  }

  delay(20);
}

static char g_usbTextBuf[128];
static uint8_t g_usbTextLen = 0;
static char g_u2TextBuf[128];
static uint8_t g_u2TextLen = 0;

void processSerialDataInput() {
  g_respStream = &SerialData;
  while (SerialData.available()) {
    uint8_t b = (uint8_t)SerialData.read();
    if (b == PROTO_SOF || g_binParserU2.state != 0) {
      processBinaryByte(g_binParserU2, b);
      continue;
    }
    if (b == '\n') {
      g_u2TextBuf[g_u2TextLen] = '\0';
      if (g_u2TextLen > 0 && g_u2TextBuf[g_u2TextLen - 1] == '\r')
        g_u2TextBuf[--g_u2TextLen] = '\0';
      if (g_u2TextLen > 0) processDebugText(g_u2TextBuf);
      g_u2TextLen = 0;
    } else if (b != '\r' && b >= 0x20) {
      if (g_u2TextLen < sizeof(g_u2TextBuf) - 1)
        g_u2TextBuf[g_u2TextLen++] = (char)b;
    }
  }
  g_respStream = &Serial;
  while (Serial.available()) {
    uint8_t b = (uint8_t)Serial.read();
    if (b == PROTO_SOF || g_binParserUSB.state != 0) {
      processBinaryByte(g_binParserUSB, b);
      continue;
    }
    if (b == '\n') {
      g_usbTextBuf[g_usbTextLen] = '\0';
      if (g_usbTextLen > 0 && g_usbTextBuf[g_usbTextLen - 1] == '\r')
        g_usbTextBuf[--g_usbTextLen] = '\0';
      if (g_usbTextLen > 0) processDebugText(g_usbTextBuf);
      g_usbTextLen = 0;
    } else if (b != '\r' && b >= 0x20) {
      if (g_usbTextLen < sizeof(g_usbTextBuf) - 1)
        g_usbTextBuf[g_usbTextLen++] = (char)b;
    }
  }
  g_respStream = &SerialData;
}

void processBinaryByte(BinParser& p, uint8_t b) {
  switch (p.state) {
    case 0: // wait SOF
      if (b == PROTO_SOF) {
        p.state = 1;
        p.idx = 0;
        p.chk = 0;
      }
      break;
    case 1: // CMD
      p.cmd = b;
      p.chk ^= b;
      p.state = 2;
      break;
    case 2: // SEQ
      p.seq = b;
      p.chk ^= b;
      p.state = 3;
      break;
    case 3: // LEN
      p.len = b;
      p.chk ^= b;
      p.idx = 0;
      if (p.len > sizeof(p.payload)) {
        p.state = 0;
      } else {
        p.state = (p.len == 0) ? 5 : 4;
      }
      break;
    case 4: // PAYLOAD
      p.payload[p.idx++] = b;
      p.chk ^= b;
      if (p.idx >= p.len) p.state = 5;
      break;
    case 5: // CHK
      if (p.chk == b) {
        handleBinaryFrame(p.cmd, p.seq, p.len, p.payload);
      } else {
        sendBinErr(p.cmd, p.seq, ERR_BAD_CHECK);
      }
      p.state = 0;
      break;
    default:
      p.state = 0;
      break;
  }
}

int mapGroupIndexToLed(int group, int idx) {
  if (group == GROUP_OUTER) {
    if (idx < 0 || idx >= OUTER_RING) return -1;
    return idx;
  }
  if (group == GROUP_INNER) {
    if (idx < 0 || idx >= INNER_RING) return -1;
    return OUTER_RING + idx;
  }
  return -1;
}

void copyStageToActive() {
  memcpy(g_ledActive, g_ledStage, sizeof(g_ledActive));
}

void clearActiveLeds() {
  for (int i = 0; i < NUM_LEDS; i++) g_ledActive[i] = {0, 0, 0, 0};
}

void renderActiveLeds() {
  for (int i = 0; i < NUM_LEDS; i++) {
    uint8_t r = (uint8_t)(((uint16_t)g_ledActive[i].r * g_ledActive[i].bri) / 255);
    uint8_t g = (uint8_t)(((uint16_t)g_ledActive[i].g * g_ledActive[i].bri) / 255);
    uint8_t b = (uint8_t)(((uint16_t)g_ledActive[i].b * g_ledActive[i].bri) / 255);
    strip.setPixelColor(i, r, g, b);
  }
  strip.show();
}

void sendBinaryFrame(uint8_t cmd, uint8_t seq, uint8_t len, const uint8_t* payload) {
  uint8_t chk = cmd ^ seq ^ len;
  g_respStream->write(PROTO_SOF);
  g_respStream->write(cmd);
  g_respStream->write(seq);
  g_respStream->write(len);
  for (uint8_t i = 0; i < len; i++) {
    chk ^= payload[i];
    g_respStream->write(payload[i]);
  }
  g_respStream->write(chk);
}

void sendBinOk(uint8_t reqCmd, uint8_t seq) {
  uint8_t payload[2] = {reqCmd, 0};
  sendBinaryFrame(BIN_ACK, seq, 2, payload);
}

void sendBinErr(uint8_t reqCmd, uint8_t seq, uint8_t errCode) {
  uint8_t payload[2] = {reqCmd, errCode};
  sendBinaryFrame(BIN_ERR, seq, 2, payload);
}

void sendTouchEvent(uint8_t type, uint16_t raw) {
  const char* evtName;
  if (type == TOUCH_EVT_PRESS)        evtName = "PRESS";
  else if (type == TOUCH_EVT_RELEASE) evtName = "RELEASE";
  else                                evtName = "HOLD";

  char textBuf[32];
  snprintf(textBuf, sizeof(textBuf), "TOUCH,%s,%u\r\n", evtName, raw);
  Serial.print(textBuf);
  SerialData.print(textBuf);

  // Binary frame only to UART2
  uint8_t payload[3] = {type, (uint8_t)(raw >> 8), (uint8_t)(raw & 0xFF)};
  Stream* saved = g_respStream;
  g_respStream = &SerialData;
  sendBinaryFrame(BIN_EVT_TOUCH, 0, 3, payload);
  g_respStream = saved;
}

void handleBinaryFrame(uint8_t cmd, uint8_t seq, uint8_t len, uint8_t* payload) {
  if (cmd == BIN_CMD_SET_ONE) {
    if (len != 6) {
      sendBinErr(cmd, seq, ERR_BAD_LEN);
      return;
    }
    int led = mapGroupIndexToLed(payload[0], payload[1]);
    if (led < 0) {
      sendBinErr(cmd, seq, ERR_BAD_INDEX);
      return;
    }
    g_ledStage[led] = {payload[2], payload[3], payload[4], payload[5]};
    sendBinOk(cmd, seq);
  } else if (cmd == BIN_CMD_SET_BLOCK) {
    if (len < 3) {
      sendBinErr(cmd, seq, ERR_BAD_LEN);
      return;
    }
    int group = payload[0];
    int start = payload[1];
    int count = payload[2];
    if (count < 0 || (3 + (int)count * 4) != (int)len) {
      sendBinErr(cmd, seq, ERR_BAD_COUNT);
      return;
    }
    for (int i = 0; i < count; i++) {
      int idx = start + i;
      int led = mapGroupIndexToLed(group, idx);
      if (led < 0) {
        sendBinErr(cmd, seq, ERR_BAD_INDEX);
        return;
      }
      int off = 3 + i * 4;
      g_ledStage[led] = {(uint8_t)payload[off], (uint8_t)payload[off + 1], (uint8_t)payload[off + 2], (uint8_t)payload[off + 3]};
    }
    sendBinOk(cmd, seq);
  } else if (cmd == BIN_CMD_SET_ALL) {
    if (len != NUM_LEDS * 4) {
      sendBinErr(cmd, seq, ERR_BAD_LEN);
      return;
    }
    for (int i = 0; i < NUM_LEDS; i++) {
      int off = i * 4;
      g_ledStage[i] = {(uint8_t)payload[off], (uint8_t)payload[off + 1], (uint8_t)payload[off + 2], (uint8_t)payload[off + 3]};
    }
    sendBinOk(cmd, seq);
  } else if (cmd == BIN_CMD_APPLY) {
    if (len != 1) {
      sendBinErr(cmd, seq, ERR_BAD_LEN);
      return;
    }
    if (payload[0] == APPLY_ENABLE_PIXEL) {
      copyStageToActive();
      g_ledDirty = true;
      sendBinOk(cmd, seq);
    } else if (payload[0] == APPLY_DISABLE_PIXEL) {
      clearActiveLeds();
      g_ledDirty = true;
      sendBinOk(cmd, seq);
    } else {
      sendBinErr(cmd, seq, ERR_BAD_MODE);
    }
  } else if (cmd == BIN_CMD_TOUCH_THR) {
    if (len != 2) {
      sendBinErr(cmd, seq, ERR_BAD_LEN);
      return;
    }
    uint16_t thr = (uint16_t)((payload[0] << 8) | payload[1]);
    g_touchThr = (uint16_t)constrain(thr, 100, 2000);
    touchAttachInterruptArg(TOUCH_PIN, onTouchISR, nullptr, g_touchThr);
    sendBinOk(cmd, seq);
  } else {
    sendBinErr(cmd, seq, ERR_BAD_CMD);
  }
}


void processDebugText(const char* line) {
  int r, g, b, bri, grp, idx, val;

  if (strncmp(line, "ALL,", 4) == 0) {

    if (sscanf(line, "ALL,%d,%d,%d,%d", &r, &g, &b, &bri) == 4) {
      for (int i = 0; i < NUM_LEDS; i++)
        g_ledStage[i] = {(uint8_t)constrain(r,0,255), (uint8_t)constrain(g,0,255),
                         (uint8_t)constrain(b,0,255), (uint8_t)constrain(bri,0,255)};
      copyStageToActive();
      g_ledDirty = true;
      ((Print*)g_respStream)->printf("OK ALL %d,%d,%d,%d\r\n", r, g, b, bri);
    } else {
      g_respStream->print("ERR format: ALL,R,G,B,BRI\r\n");
    }

  } else if (strncmp(line, "ONE,", 4) == 0) {
    if (sscanf(line, "ONE,%d,%d,%d,%d,%d,%d", &grp, &idx, &r, &g, &b, &bri) == 6) {
      int led = mapGroupIndexToLed(grp, idx);
      if (led < 0) {
        g_respStream->print("ERR bad index\r\n");
        return;
      }
      for (int i = 0; i < NUM_LEDS; i++) g_ledStage[i] = {0, 0, 0, 0};
      g_ledStage[led] = {(uint8_t)constrain(r,0,255), (uint8_t)constrain(g,0,255),
                         (uint8_t)constrain(b,0,255), (uint8_t)constrain(bri,0,255)};
      copyStageToActive();
      g_ledDirty = true;
      ((Print*)g_respStream)->printf("OK ONE grp=%d idx=%d %d,%d,%d,%d\r\n", grp, idx, r, g, b, bri);
    } else {
      g_respStream->print("ERR format: ONE,grp,idx,R,G,B,BRI\r\n");
    }

  } else if (strncmp(line, "BRI,", 4) == 0) {
    if (sscanf(line, "BRI,%d", &val) == 1) {
      val = constrain(val, 0, 255);
      for (int i = 0; i < NUM_LEDS; i++)
        g_ledStage[i].bri = (uint8_t)val;
      copyStageToActive();
      g_ledDirty = true;
      ((Print*)g_respStream)->printf("OK BRI %d\r\n", val);
    } else {
      g_respStream->print("ERR format: BRI,0-255\r\n");
    }

  } else if (strcmp(line, "OFF") == 0) {
    clearActiveLeds();
    g_ledDirty = true;
    g_respStream->print("OK OFF\r\n");

  } else if (strncmp(line, "THR,", 4) == 0) {
    if (sscanf(line, "THR,%d", &val) == 1) {
      g_touchThr = (uint16_t)constrain(val, 100, 2000);
      touchAttachInterruptArg(TOUCH_PIN, onTouchISR, nullptr, g_touchThr);
      ((Print*)g_respStream)->printf("OK THR %d\r\n", g_touchThr);
    } else {
      g_respStream->print("ERR format: THR,100-2000\r\n");
    }

  } else if (strncmp(line, "RAINBOW", 7) == 0) {
    int rbri = 200;
    sscanf(line, "RAINBOW,%d", &rbri);
    rbri = constrain(rbri, 0, 255);
    for (int i = 0; i < NUM_LEDS; i++) {
      uint16_t hue = (uint16_t)((uint32_t)i * 65536 / NUM_LEDS);
      uint32_t c = strip.ColorHSV(hue, 255, 255);
      c = strip.gamma32(c);
      g_ledStage[i] = {(uint8_t)((c >> 16) & 0xFF), (uint8_t)((c >> 8) & 0xFF),
                        (uint8_t)(c & 0xFF), (uint8_t)rbri};
    }
    copyStageToActive();
    g_ledDirty = true;
    ((Print*)g_respStream)->printf("OK RAINBOW bri=%d\r\n", rbri);

  } else if (strcmp(line, "HELP") == 0) {
    g_respStream->print("ALL,R,G,B,BRI   - set all 40 LEDs and apply\r\n");
    g_respStream->print("ONE,grp,idx,R,G,B,BRI - set one LED and apply\r\n");
    g_respStream->print("BRI,val         - set all LEDs brightness\r\n");
    g_respStream->print("OFF             - turn off all LEDs\r\n");
    g_respStream->print("THR,val         - set touch threshold (100-2000)\r\n");
    g_respStream->print("RAINBOW[,BRI]   - rainbow gradient (default BRI=200)\r\n");
    g_respStream->print("HELP            - show this help\r\n");

  } else {
    ((Print*)g_respStream)->printf("ERR unknown: %s\r\n", line);
  }
}
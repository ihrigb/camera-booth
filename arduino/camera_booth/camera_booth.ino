const int startCountdown = 5;
const byte opto_focus = 2;
const byte opto_shutter = 3;
const byte button = 11;

// seven-segment pins
const byte a = 4;
const byte b = 5;
const byte c = 6;
const byte d = 7;
const byte e = 8;
const byte f = 9;
const byte g = 10;

const byte sevenSegPins[7] = {a, b, c, d, e, f, g};

boolean trigger = false;
int buttonState;
int lastButtonState = LOW;
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

void on(byte pin) {
  digitalWrite(pin, HIGH);
}

void off(byte pin) {
  digitalWrite(pin, LOW);
}

void displayDigit(int digit) {
  // segment a
  if (digit != 1 && digit != 4) {
    on(a);
  } else {
    off(a);
  }

  // segment b
  if (digit != 5 && digit != 6) {
    on(b);
  } else {
    off(b);
  }

  // segment c
  if (digit != 2) {
    on(c);
  } else {
    off(c);
  }

  // segment d
  if (digit != 1 && digit != 4 && digit != 7) {
    on(d);
  } else {
    off(d);
  }

  // segment e
  if (digit == 2 || digit == 6 || digit == 8 || digit == 0) {
    on(e);
  } else {
    off(e);
  }

  // segment f
  if (digit != 1 && digit != 2 && digit != 3 && digit != 7) {
    on(f);
  } else {
    off(f);
  }

  // segment g
  if (digit != 0 && digit != 1 && digit != 7) {
    on(g);
  } else {
    off(g);
  }
}

void turnLedOff() {
  for (byte pin = 0; pin < (sizeof(sevenSegPins) / sizeof(byte)); pin++) {
    off(sevenSegPins[pin]);
  }
}

void focus() {
  on(opto_focus);
}

void shutter() {
  on(opto_shutter);
}

void resetCamera() {
  off(opto_shutter);
  off(opto_focus);
}

void takePhoto() {
  for (int i = startCountdown; i >= 0; i--) {
    displayDigit(i);
    if (i == 2) {
      focus();
    }
    if (i == 0) {
      shutter();
      delay(200);
      resetCamera();
      delay(800);
      break;
    }
    delay(1000);
  }
  turnLedOff();
}

void setup() {
  // put your setup code here, to run once:
  //Serial.begin(115200);
  pinMode(button, INPUT);
  pinMode(opto_focus, OUTPUT);
  pinMode(opto_shutter, OUTPUT);

  for (byte pin = 0; pin < (sizeof(sevenSegPins) / sizeof(byte)); pin++) {
    pinMode(sevenSegPins[pin], OUTPUT);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  int reading = digitalRead(button);

  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;

      if (buttonState == HIGH) {
        trigger = true;
      }
    }
  }

  lastButtonState = reading;
  
  if (trigger) {
    trigger = false;
    takePhoto();
  }
}

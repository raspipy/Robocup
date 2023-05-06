#include <Arduino.h>
#include "Header.h"

const uint8_t BaseSpeed = 60;
const float Sensitivy1 = 3.0;
const float Sensitivy2 = 4.0;

float Err = 0.0;
float LastErr = 0.0;

void setup() {
  SetupMotor();
  SetupLineSensor();
  EnableLed();
}

void loop() {
  SetMotorSpeedL(-100);
  SetMotorSpeedR(100);
}
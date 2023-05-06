#include <Arduino.h>
#include "Header.h"

void setup() {
  SetupMotor();
}

void loop() {
  SetMotorSpeedL(-100);
  SetMotorSpeedR(100);
}
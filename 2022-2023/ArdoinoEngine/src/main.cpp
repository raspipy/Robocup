#include <Arduino.h>
#include "header.h"
#include "logger.cpp"


void setup() {
  
  Serial.begin(9600);

  setupMotor();
  SetMotorSpeed(0,255);
  SetMotorSpeed(1,255);
}
void loop(){
  // attachInterrupt(digitalPinToInterrupt(69), ) // uncomment deze code voor hardware interrupts support
  Serial.println("The odo is woko!");
}





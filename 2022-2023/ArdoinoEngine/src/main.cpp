#include <Arduino.h>
#include "header.h"

void setup() {
  
  Serial.begin(9600);

  setupMotor();
  SetMotorSpeed(0,255);
  SetMotorSpeed(1,255);
}
void loop(){
  Serial.println("The odo is woko!");
}
#include <Arduino.h>
#include <header.h>

const uint8_t pwm_a1 = 3;
const uint8_t pwm_a2 = 4;
const uint8_t pwm_b1 = 5;
const uint8_t pwm_b2 = 2;

void SetupMotor(){
    pinMode(pwm_a1, OUTPUT);
    pinMode(pwm_a2, OUTPUT);
    pinMode(pwm_b1, OUTPUT);
    pinMode(pwm_b2, OUTPUT);
}
void SetMotorSpeedL(int speed){
  if(abs(speed)>255){
    speed = 255*(abs(speed)/speed);
  }
  if(speed < 0){
    analogWrite(pwm_a1, 0); 
    analogWrite(pwm_a2, abs(speed));  
  }
  else{
    analogWrite(pwm_a1, speed);
    analogWrite(pwm_a2, 0);
  }
}
void SetMotorSpeedR(int speed){
  if(abs(speed)>255){
    speed = 255*(abs(speed)/speed);
  }
  if(speed < 0){
    analogWrite(pwm_b1, 0); 
    analogWrite(pwm_b2, abs(speed));  
  }
  else{
    analogWrite(pwm_b1, speed);
    analogWrite(pwm_b2, 0);  
  }
}
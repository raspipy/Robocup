#include <Arduino.h>
#include <header.h>

const uint8_t pwm_a1 = 3;
const uint8_t pwm_a2 = 4;
const uint8_t pwm_b1 = 5;
const uint8_t pwm_b2 = 2;
const uint8_t EncAPin = 21;
const uint8_t EncBPin = 19;

unsigned long EncACount = 0;
unsigned long EncBCount = 0;

void SetupMotor(){
    pinMode(pwm_a1, OUTPUT);
    pinMode(pwm_a2, OUTPUT);
    pinMode(pwm_b1, OUTPUT);
    pinMode(pwm_b2, OUTPUT);
    attachInterrupt(digitalPinToInterrupt(EncAPin),EncoderA,RISING);
    attachInterrupt(digitalPinToInterrupt(EncBPin),EncoderB,RISING);
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
void EncoderA(){
  EncACount ++;
}
void EncoderB(){
  EncBCount ++;
}
void TurnRight(){
  SetMotorSpeedL(0);
  SetMotorSpeedR(0);

  unsigned long StartA = EncACount;
  SetMotorSpeedL(100);
  while(EncACount - StartA < 200){
    Serial.println("Hello the");
    continue;
  }
  SetMotorSpeedL(0);
}
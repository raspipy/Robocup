#include <Arduino.h>
#include <header.h>
#include "math.h"

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
  while(EncACount - StartA < 147){
    Serial.print("");
  }
  SetMotorSpeedL(0);
}
void TurnLeft(){
  SetMotorSpeedL(0);
  SetMotorSpeedR(0);

  unsigned long StartB = EncBCount;
  SetMotorSpeedR(100);
  while(EncBCount - StartB < 137){
    Serial.print("");
  }
  SetMotorSpeedR(0);
}
void MoveForward(unsigned long dist){
  for(int i = 0;i<dist;i++){
    SetMotorSpeedL(0);
    SetMotorSpeedR(0);
    delay(50);
    unsigned long StartA = EncACount;
    unsigned long StartB = EncBCount;

    unsigned long DifA = EncACount-StartA;
    unsigned long DifB = EncBCount-StartB;

    SetMotorSpeedL(90);
    SetMotorSpeedR(75);

    while(min(DifA,DifB)<30){
      DifA = EncACount-StartA;
      DifB = EncBCount-StartB;
      if(DifA>=30){
        SetMotorSpeedL(0);
      }
      if(DifB>=30){
        SetMotorSpeedR(0);
      }
      Serial.print("");
    }
  }
}

void turn45right(){
  SetMotorSpeedL(0);
  SetMotorSpeedR(0);

  unsigned long StartA = EncACount;
  SetMotorSpeedL(100);
  while(EncACount - StartA < 74){
    Serial.print("");
  }
  SetMotorSpeedL(0);
}
void turn45left(){
  SetMotorSpeedL(0);
  SetMotorSpeedR(0);

  unsigned long StartB = EncBCount;
  SetMotorSpeedR(100);
  while(EncBCount - StartB < 69){
    Serial.print("");
  }
  SetMotorSpeedR(0);
}
void SeekForBlick(){
  SetMotorSpeedL(0);
  SetMotorSpeedR(0);
  
  delay(1000);
  TurnRight();

  delay(500);
  MoveForward(2);

  delay(500);
  TurnLeft();

  delay(500);
  MoveForward(7);

  delay(500);
  TurnLeft();
  
  delay(500);
  MoveForward(3);

  delay(500);
  TurnRight();

  delay(1000);
}

void empty() {}
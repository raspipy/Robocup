#include <Arduino.h>
#include "header.h"

#define ENA 9
#define ENB 3
#define IN1 13
#define IN2 12
#define IN3 11
#define IN4 10

void setupMotor() {
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}



void SetMotorSpeed(int speed,int motor){
  if (speed > 0){
    ConfigMotor(motor,"forward");
    
    if (motor == 0){
      analogWrite(ENA,speed);
    }
    if (motor == 1){
      analogWrite(ENB,speed);
    }
  }
  if (speed < 0){
    ConfigMotor(motor,"backward");
    
    if (motor == 0){
      analogWrite(ENA,-speed);
    }
    if (motor == 1){
      analogWrite(ENB,-speed);
    }
  }
  if (speed==0){
    if (motor == 0){
      analogWrite(ENA,0);
    }
    if (motor == 1){
      analogWrite(ENB,0);
    }
  }
}


void ConfigMotor(int Engine,String mode){
  if(Engine == 0){
    if (mode == "forward"){;
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
    }
    else{
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
    }
  }
  else{
    if (mode == "forward"){
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, HIGH);
    }
    else{
      digitalWrite(IN3, HIGH);
      digitalWrite(IN4, LOW);
    }
  }
}
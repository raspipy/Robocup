#include <Arduino.h>
#include <header.h>

/*
important variables tweak before start
*/
const uint8_t BaseSpeed = 60;
const float Sensitivy1 = 3.0;
const float Sensitivy2 = 4.0;
float GreenTurnCooldown = 1000; //millis
float TurnAmount = 500; //Time the motors are turning with TurnSpeed when green is detected
float TurnSpeed = 50;

/*
Dont touch these ones
*/
float Err = 0.0;
float LastErr = 0.0;
float LastGreenTurn = 0.0;
float LastGreen = 0.0;
bool CanRide = true;

void setup() {
  Serial.begin(9600);
  
  //ColorSensor
  SetupColorSensor();
  

  //motor
  SetupMotor();

  //Linesensor
  SetupLineSensor();
  EnableLed();

  delay(3000);
  SetMotorSpeedL(-100);
  SetMotorSpeedR(100);
  Serial.println("start calb.(line)");
  AutoCalibrate(5000);
  Serial.println("end calb.(line)");
  SetMotorSpeedL(0);
  SetMotorSpeedR(0);
  delay(3000);
  
}

void loop() {
  CanRide = true;

  int c0 = ReadColorsens0();
  int c1 = ReadColorsens1();

  LastErr = Err;
  Err = GetError();

  
  if((c0 == 2 && c1 == 2) && CanRide){
    CanRide = false;
    SetMotorSpeedL(0);
    SetMotorSpeedR(0);
    //DestroyCan();
  }
  /*

  
  else if(c0 == 2 && c1 != 2){
    if(LastGreenTurn+GreenTurnCooldown < millis()){
      SetMotorSpeedR(TurnSpeed);
      SetMotorSpeedL(-TurnSpeed);
      delay(TurnAmount);
      SetMotorSpeedL(0);
      SetMotorSpeedR(0);
      LastGreenTurn = millis();
    }
  }

  
  else if(c0 != 2 && c1 == 2){
    if(LastGreenTurn+GreenTurnCooldown < millis()){
      SetMotorSpeedL(TurnSpeed);
      SetMotorSpeedR(-TurnSpeed);
      delay(TurnAmount);
      SetMotorSpeedL(0);
      SetMotorSpeedR(0);
      LastGreenTurn = millis();
    }
  }*/
  
  
  //if(CanRide){
  //  SetMotorSpeedL(BaseSpeed+(Err*Sensitivy1+(Err-LastErr)*Sensitivy2));
  //  SetMotorSpeedR(BaseSpeed-(Err*Sensitivy1+(Err-LastErr)*Sensitivy2));
  //}
  TurnRight();
  delay(5000);
  

}



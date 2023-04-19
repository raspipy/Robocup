#include <Arduino.h>

//linesens.cpp        
void EnableLed();
void AutoCalibrate(int);
void UpdateRawData();
void UpdateSensorData();
void CalculateError();
float GetError();

int16_t GetRawData();

//motor.cpp
void SetupMotor();
void SetMotorSpeedR(int);
void SetMotorSpeedL(int);
void EncoderA();
void EncoderB();
void TurnRight();

//ColorSensor.cpp
void SetupColorSensor();
int ReadPWM(uint8_t);
void LoadProm();
int ReadColorsens0();
int ReadColorsens1();
int readIntFromEEPROM(int);
void writeIntIntoEEPROM(int,int);
void CalbWhite();
void CalbBlack();
void CalbGreen();

//can.cpp
float GetDist();
void SetupLineSensor();
void DestroyCan();
#include <Arduino.h>

//linesens.cpp        
void EnableLed();
void AutoCalibrate(int);
void UpdateRawData();
void UpdateSensorData();
void CalculateError();
float GetError();
int16_t GetRawData();


// Main.cpp
int Drive();

//Reciever.cpp
void StartCommands();

//motor.cpp
void SetupMotor();
void SetMotorSpeedR(int);
void SetMotorSpeedL(int);

//ColorSensor.cpp
void SetupColorSensor();
int ReadPWM(uint8_t);
void WriteProm();
void Callibrate();
void LoadProm();
int ReadColorsens0();
int ReadColorsens1();

//can.cpp
float GetDist();
void SetupLineSensor();
void DestroyCan();
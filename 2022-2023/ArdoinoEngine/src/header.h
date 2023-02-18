#include <Arduino.h>
void setupLineSensor();
float getPos();
void updateLineColor();
void updatePosition();
void updateRawData();
void updateWhiteCalibration();
void updateBlackCalibration();
void setColor(int color);
void Calibraite();
void setupMotor();
void SetMotorSpeed(int, int);
void ConfigMotor(int, String);
long microsecondsToInches(long);
long microsecondsToCentimeters(long);
long Distance();
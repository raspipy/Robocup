#include <Arduino.h>
#include <LinkedList.h>
// deze lib's moet je niet meer importen in andere files zolang header/h geimporteerd is



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
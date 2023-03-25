#include <Arduino.h>
#include "header.h"
#define led 22  //digital pin where conected whit lineSensor: QRE-LED
#include <math.h>

int lineSensorPins[8] = {A0,A1,A2,A3,A4,A5,A6,A7}; //the analog pins conected to the sensor

int lineResults[8] = {0,0,0,0,0,0,0,0};

int whiteCalibration[8] = {950,950,950,950,950,950,950,950}; //white calibartion
int blackCalibration[8] = {900,900,900,900,900,900,900,900}; //black calibration

double position = 0; //position | -35:  left | 35: right | 0: forward |

int coloroutput[8] = {0,0,0,1,1,0,0,0}; //list of ints with value 0 or 1

int ColorSensorColor0 = 0;
int ColorSensorColor1 = 0;

void setupLineSensor(){

  //color sensor
  pinMode(ColorSensorColor0,OUTPUT);
  pinMode(ColorSensorColor1,OUTPUT);

  //enable lineSensors
  pinMode(led,OUTPUT);
  digitalWrite(led,HIGH);
  pinMode(24,OUTPUT);
  pinMode(26,OUTPUT);
  digitalWrite(24,LOW);
  digitalWrite(26,LOW);
}

float getPos(){
    updateRawData();
    updateLineColor();
    updatePosition();
    return position;
}


void updateLineColor(){
  for (int i = 0; i < (sizeof(lineResults) / sizeof(int))-1; i = i + 1) {  //loop over a integer array
    if (abs(lineResults[i] - blackCalibration[i]) < abs(lineResults[i] - whiteCalibration[i])){ //whit or black?
      coloroutput[i] = 1; //black
    }
    else{
      coloroutput[i] = 0; //white
    }
  }
}

void updatePosition(){
  double nomineter = (0*coloroutput[0]) + (10*coloroutput[1]) + (20*coloroutput[2]) + (30*coloroutput[3]) + (40*coloroutput[4]) + (50*coloroutput[5]) + (60*coloroutput[6]) + (70*coloroutput[7]);
  double denomineter = coloroutput[0] + coloroutput[1] + coloroutput[2] + coloroutput[3] + coloroutput[4] + coloroutput[5] + coloroutput[6] + coloroutput[7];

  if (denomineter != 0){
    position = (nomineter/denomineter)-35;
  }
}

void updateRawData(){
  //why each appart? because c++ is a thing.
  
  lineResults[0] = analogRead(A0);
  lineResults[1] = analogRead(A1);
  lineResults[2] = analogRead(A2);
  lineResults[3] = analogRead(A3);
  lineResults[4] = analogRead(A4);
  lineResults[5] = analogRead(A5);
  lineResults[6] = analogRead(A6);
  lineResults[7] = analogRead(A7);
}
void updateWhiteCalibration(){
  whiteCalibration[0] = analogRead(A0);
  whiteCalibration[1] = analogRead(A1);
  whiteCalibration[2] = analogRead(A2);
  whiteCalibration[3] = analogRead(A3);
  whiteCalibration[4] = analogRead(A4);
  whiteCalibration[5] = analogRead(A5);
  whiteCalibration[6] = analogRead(A6);
  whiteCalibration[7] = analogRead(A7);
}
void updateBlackCalibration(){
  blackCalibration[0] = analogRead(A0);
  blackCalibration[1] = analogRead(A1);
  blackCalibration[2] = analogRead(A2);
  blackCalibration[3] = analogRead(A3);
  blackCalibration[4] = analogRead(A4);
  blackCalibration[5] = analogRead(A5);
  blackCalibration[6] = analogRead(A6);
  blackCalibration[7] = analogRead(A7);
}

void setColor(int color){
  if(color == 0){
    digitalWrite(ColorSensorColor0,LOW);
    digitalWrite(ColorSensorColor1,LOW);
  }
  if(color == 1){
    digitalWrite(ColorSensorColor0,LOW);
    digitalWrite(ColorSensorColor1,HIGH);
  }
  if(color == 2){
    digitalWrite(ColorSensorColor0,HIGH);
    digitalWrite(ColorSensorColor1,LOW);
  }
  if(color == 3){
    digitalWrite(ColorSensorColor0,HIGH);
    digitalWrite(ColorSensorColor1,HIGH);
  }
}

void Calibraite(){
  digitalWrite(24,LOW);
  digitalWrite(26,LOW);
  delay(100);
  digitalWrite(24,HIGH);
  digitalWrite(26,LOW);
  delay(5000);
  updateWhiteCalibration();
  digitalWrite(24,LOW);
  digitalWrite(26,LOW);
  delay(5000);
  digitalWrite(24,LOW);
  digitalWrite(26,HIGH);
  delay(5000);
  updateBlackCalibration();
  digitalWrite(24,LOW);
  digitalWrite(26,LOW);
}
#include <arduino.h>
int pwm_a = 3;
int pwm_b = 9;
int dir_a = 2;
int dir_b = 8;

float avg = 0.0;

#define led 50  //digital pin where conected whit lineSensor: QRE-LED

#include <math.h>

int lineSensorPins[8] = {A8,A9,A1,A11,A12,A13,A14,A15}; //the analog pins conected to the sensor

int lineResults[8] = {0,0,0,0,0,0,0,0};

int whiteCalibration[8] = {650,650,650,650,650,650,650,650}; //white calibartion
int blackCalibration[8] = {950,950,950,950,950,950,950,950}; //black calibration

double position = 0; //position | -35:  left | 35: right | 0: forward |
int coloroutput[8] = {0,0,0,1,1,0,0,0}; //list of ints with value 0 or 1

float ColorSensorColor0 = 0;
float ColorSensorColor1 = 0;
float derivative = 0;

int kp = 10;
int kd = 10;
float prev_error  = 0;
float derivative = 0;
int basespeed = 50;

void setup(){
  setupLineSensor();
  Serial.begin(9600);
}
const int pingPin = 7;

long Distance(){
    long duration;

    pinMode(pingPin, OUTPUT);
    digitalWrite(pingPin, LOW);
    delayMicroseconds(2);
    digitalWrite(pingPin, HIGH);
    delayMicroseconds(5);
    digitalWrite(pingPin, LOW);

    pinMode(pingPin, INPUT);
    duration = pulseIn(pingPin, HIGH);

    return(microsecondsToCentimeters(duration));
}

long microsecondsToInches(long microseconds) {
  return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
  return microseconds / 29 / 2;
}
int m1;
int m2;
void loop(){
  getPos();

  derivative = kd * (position - prev_error);
  prev_error = position;
  m1 = basespeed + kp * position + derivative;
  m2 = basespeed - kp * position - derivative;
}

void setupLineSensor(){

  //color sensor
  pinMode(ColorSensorColor0,OUTPUT);
  pinMode(ColorSensorColor1,OUTPUT);

  //enable lineSensors
  pinMode(led,OUTPUT);
  digitalWrite(led,HIGH);
  /*pinMode(24,OUTPUT);
  pinMode(26,OUTPUT);
  digitalWrite(24,LOW);
  digitalWrite(26,LOW);*/
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
  
  lineResults[0] = analogRead(lineSensorPins[0]);
  lineResults[1] = analogRead(lineSensorPins[1]);
  lineResults[2] = analogRead(lineSensorPins[2]);
  lineResults[3] = analogRead(lineSensorPins[3]);
  lineResults[4] = analogRead(lineSensorPins[4]);
  lineResults[5] = analogRead(lineSensorPins[5]);
  lineResults[6] = analogRead(lineSensorPins[6]);
  lineResults[7] = analogRead(lineSensorPins[7]);
}
void updateWhiteCalibration(){
  whiteCalibration[0] = analogRead(lineSensorPins[0]);
  whiteCalibration[1] = analogRead(lineSensorPins[1]);
  whiteCalibration[2] = analogRead(lineSensorPins[2]);
  whiteCalibration[3] = analogRead(lineSensorPins[3]);
  whiteCalibration[4] = analogRead(lineSensorPins[4]);
  whiteCalibration[5] = analogRead(lineSensorPins[5]);
  whiteCalibration[6] = analogRead(lineSensorPins[6]);
  whiteCalibration[7] = analogRead(lineSensorPins[7]);
}
void updateBlackCalibration(){
  blackCalibration[0] = analogRead(lineSensorPins[0]);
  blackCalibration[1] = analogRead(lineSensorPins[1]);
  blackCalibration[2] = analogRead(lineSensorPins[2]);
  blackCalibration[3] = analogRead(lineSensorPins[3]);
  blackCalibration[4] = analogRead(lineSensorPins[4]);
  blackCalibration[5] = analogRead(lineSensorPins[5]);
  blackCalibration[6] = analogRead(lineSensorPins[6]);
  blackCalibration[7] = analogRead(lineSensorPins[7]);
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

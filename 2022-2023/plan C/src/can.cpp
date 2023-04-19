#include <Arduino.h>
#include <header.h>
const uint8_t dist_pin = 10;

void SetupLineSensor(){
    pinMode(dist_pin,INPUT);
}

float GetDist(){
    int16_t t = pulseIn(dist_pin, HIGH);
 
  if (t == 0)
  {
    return 100000000; //timeout
  }
  else if (t > 1850)
  {
    return 100000000; // No detection.
  }
  else
  {
    // Valid pulse width reading. Convert pulse width in microseconds to distance in millimeters.
    int16_t d = (t - 1000) * 3 / 4;
 
    // Limit minimum distance to 0.
    if (d < 0) { d = 0; } 
  
    return d; //dist in mm
  }
}

void DestroyCan(){
    Serial.println("Destroying can!");
    SetMotorSpeedL(-60);
    SetMotorSpeedR(60);
    while (GetDist()>200){;}
    SetMotorSpeedL(0);
    SetMotorSpeedR(0);
    delay(10000);
}
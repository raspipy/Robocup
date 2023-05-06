
#include <Arduino.h>
#include <header.h>

#define NUM_SENSORS 8

const uint8_t LedPin = 22;
const uint8_t SensorPins[NUM_SENSORS] = {A0,A1,A2,A3,A4,A5,A6,A7};

int16_t MinCalibration[NUM_SENSORS] = {1023,1023,1023,1023,1023,1023,1023,1023};
int16_t MaxCalibration[NUM_SENSORS] = {0,0,0,0,0,0,0,0};

int16_t RawSensorData[NUM_SENSORS] = {0,0,0,0,0,0,0,0};

bool SensorData[NUM_SENSORS] = {0,0,0,0,0,0,0,0};
float Error = 0.0;

void EnableLed(){
    pinMode(LedPin,OUTPUT);
    digitalWrite(LedPin,HIGH);
}

void AutoCalibrate(int Delta){
    uint32_t StartTime = millis();
    while(StartTime+Delta>millis()){
        int16_t CurrentValue = 0;

        for(uint8_t i=0;i<NUM_SENSORS;i++){
            CurrentValue = analogRead(SensorPins[i]);

            if(CurrentValue<MinCalibration[i]){
                MinCalibration[i] = CurrentValue;
            }

            if(CurrentValue>MaxCalibration[i]){
                MaxCalibration[i] = CurrentValue;
            }
        }
    }
    Serial.print("Min Calibration Values:\t");
    for (uint8_t i = 0; i < NUM_SENSORS; i++) {
        Serial.print(MinCalibration[i]);
        Serial.print("\t");
    }
    Serial.print("\n");
    Serial.print("Max Calibration Values:\t");
    for (uint8_t i = 0; i < NUM_SENSORS; i++) {
        Serial.print(MaxCalibration[i]);
        Serial.print("\t");
    }
    Serial.print("\n");
}

void UpdateRawData(){
    for(uint8_t i = 0;i<NUM_SENSORS;i++){
        RawSensorData[i] = analogRead(SensorPins[i]);
    }
}

int16_t GetRawData(){
    return RawSensorData[0];
}

void UpdateSensorData(){
    for(uint8_t i = 0;i<NUM_SENSORS;i++){
        if(abs(MinCalibration[i]-RawSensorData[i])<abs(MaxCalibration[i]-RawSensorData[i])){
            SensorData[i] = 0;
        } else {
            SensorData[i] = 1;
        }
    }
}

void CalculateError(){
    double Numerator = 0.0;
    double Denominator = 0.0;
    for(uint8_t i = 0; i<NUM_SENSORS; i++){
        Numerator += (i*10)*SensorData[i];
        Denominator += SensorData[i];
    }
    if(Denominator!=0.0){
        Error = Numerator/Denominator-35;
    }
}

float GetError(){
    UpdateRawData();
    UpdateSensorData();
    CalculateError();
    return Error;
}
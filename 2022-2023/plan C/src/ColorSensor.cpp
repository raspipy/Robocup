#include <Arduino.h>
#include <header.h>
#include <EEPROM.h>

const uint8_t TCS_OUT_0 = 32;
const uint8_t TCS_OUT_1 = 31;
const uint8_t TCS_LED = 33;
const uint8_t TCS_S0 = 34;
const uint8_t TCS_S1 = 35;
const uint8_t TCS_S2 = 36;
const uint8_t TCS_S3 = 37;
const uint8_t TCS_OE = 13;

long ColorBlackAVGsens0 = 0;
long ColorWhiteAVGsens0 = 0;
long ColorGreenAVGsens0 = 0;

long ColorBlackAVGsens1 = 0;
long ColorWhiteAVGsens1 = 0;
long ColorGreenAVGsens1 = 0;

void SetupColorSensor(){

    pinMode(TCS_S0,OUTPUT);
    pinMode(TCS_S1,OUTPUT);
    pinMode(TCS_S2,OUTPUT);
    pinMode(TCS_S3,OUTPUT);
    pinMode(TCS_LED,OUTPUT);
    pinMode(TCS_OE,OUTPUT);

    pinMode(TCS_OUT_0,INPUT);
    pinMode(TCS_OUT_1,INPUT);


    digitalWrite(TCS_LED,HIGH);
    digitalWrite(TCS_OE,LOW);

    //Output frequency 20%
    digitalWrite(TCS_S0,HIGH);
    digitalWrite(TCS_S1,LOW);

    //filter
    digitalWrite(TCS_S2,HIGH);
    digitalWrite(TCS_S3,HIGH);

}

void Callibrate(int a){
    if (a == 3){
        for(int i = 0;i<5000;i++){
            ColorGreenAVGsens0 += ReadPWM(TCS_OUT_0);
            ColorGreenAVGsens1 += ReadPWM(TCS_OUT_1);
        }
        ColorGreenAVGsens0 /= 5000;
        ColorGreenAVGsens1 /= 5000;
        Serial.println("Done.");

    }
    if (a == 4){
        for(int i = 0;i<5000;i++){
                ColorWhiteAVGsens0 += ReadPWM(TCS_OUT_0);
                ColorWhiteAVGsens1 += ReadPWM(TCS_OUT_1);
            }
        ColorWhiteAVGsens0 /= 5000;
        ColorWhiteAVGsens1 /= 5000;

        Serial.println("Done.");

    }
    if (a == 5){
        for(int i = 0;i<5000;i++){
            ColorBlackAVGsens0 += ReadPWM(TCS_OUT_0);
            
            ColorBlackAVGsens1 += ReadPWM(TCS_OUT_1);
            }
        Serial.println(ColorBlackAVGsens0);
        ColorBlackAVGsens0 /= 5000;
        Serial.println("result");
        Serial.println(ColorBlackAVGsens1);
    }

}

void WriteProm(){
    EEPROM.write(0+10,(uint8_t) ColorBlackAVGsens0);
    EEPROM.write(1+10,(uint8_t) ColorBlackAVGsens1);
    EEPROM.write(2+10,(uint8_t) ColorGreenAVGsens0);
    EEPROM.write(3+10,(uint8_t) ColorGreenAVGsens1);
    EEPROM.write(4+10,(uint8_t) ColorWhiteAVGsens0);
    EEPROM.write(5+10,(uint8_t) ColorWhiteAVGsens1);
}

void LoadProm(){
    ColorBlackAVGsens0 = EEPROM.read(0+10);
    ColorBlackAVGsens1 = EEPROM.read(1+10);
    ColorGreenAVGsens0 = EEPROM.read(2+10);
    ColorGreenAVGsens1 = EEPROM.read(3+10);
    ColorWhiteAVGsens0 = EEPROM.read(4+10);
    ColorWhiteAVGsens1 = EEPROM.read(5+10);
}

int ReadPWM(uint8_t readpin){
    return pulseIn(readpin, LOW);
}

int ReadColorsens0(){
    //Returns 0 if black
    //Returns 1 if white
    //Returns 2 if green
    int Value = ReadPWM(TCS_OUT_0);
    //Serial.print("Raw value ColorSens0: ");
    //Serial.println(Value);

    int DiffBlack = abs(ColorBlackAVGsens0-Value);
    int DiffWhite = abs(ColorWhiteAVGsens0-Value);
    int DiffGreen = abs(ColorGreenAVGsens0-Value);

    if(DiffBlack < DiffWhite && DiffBlack < DiffGreen){
        return 0;
    }
    else if(DiffWhite < DiffBlack && DiffWhite < DiffGreen){
        return 1;
    }
    else{return 2;}
}

int ReadColorsens1(){
    //Returns 0 if black
    //Returns 1 if white
    //Returns 2 if green
    int Value = ReadPWM(TCS_OUT_1);

    int DiffBlack = abs(ColorBlackAVGsens1-Value);
    int DiffWhite = abs(ColorWhiteAVGsens1-Value);
    int DiffGreen = abs(ColorGreenAVGsens1-Value);

    if(DiffBlack < DiffWhite && DiffBlack < DiffGreen){
        return 0;
    }
    else if(DiffWhite < DiffBlack && DiffWhite < DiffGreen){
        return 1;
    }
    else{return 2;}
}
/*

        Made with <3 by raspipy


*/

#include <Arduino.h>
#include <header.h>
int incomingByte;
int LastInstruction;

void StartCommands(){

    if (Serial.available() > 0){
    incomingByte = Serial.parseInt();
    LastInstruction = incomingByte;
    if (LastInstruction){
        Drive();
    }
    else if (!LastInstruction){

    }
    else {
        Callibrate(LastInstruction)
    }
        }
    
}


//motor.cpp
void SetupMotor();
void SetMotorSpeedL(int);
void SetMotorSpeedR(int);
void EncoderA();
void EncoderB();
void TurnRight();
void TurnLeft();
void MoveForward(unsigned long);
void turn45right();
void turn45left();
void SeekForBlick();
void empty();

//linesensor.cpp
void EnableLed();
void AutoCalibrate(int);
void UpdateRawData();
int16_t GetRawData();
void UpdateSensorData();
void CalculateError();
float GetError();
import RPi.GPIO as pi

pi.setmode(pi.BOARD)

class motor:
    
    def __init__(self,pins, minumun_speed):
        
        self.pin_vooruit = pins[0]
        self.pin_achteruit = pins[1]
        self.pin_pwm = pins[2]
        self.minumun_speed = minumun_speed
        
        pin_toggle = pins[3]
        pi.setup(pin_toggle,pi.OUT)
        pi.output(pin_toggle,1)
        
        pi.setup(self.pin_vooruit,pi.OUT)
        pi.setup(self.pin_achteruit,pi.OUT)
        
        pi.setup(self.pin_pwm,pi.OUT)
        self.pwm = pi.PWM(self.pin_pwm, 1000)
        self.pwm.start(0)
        
    def drive(self,speed):
        if speed >= 0:
            pi.output(self.pin_vooruit,1)
            pi.output(self.pin_achteruit,0)
        else:
            pi.output(self.pin_vooruit,0)
            pi.output(self.pin_achteruit,1)
            speed *= -1
        if speed > 0 and speed < self.minumun_speed:
            speed = self.minumun_speed

        self.pwm.ChangeDutyCycle(speed)
        
        
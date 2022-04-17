import RPi.GPIO as GPIO
import time
import random
from classes.ultrasonesensor import ultrasonesensor
from classes.lijnsensor import lijnsensor
from classes.motor import motor
from classes.kleurensensor import kleurensensor

GPIO.setwarnings(False)

lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
print(lijnsensor.readData())

motor1 = motor([35,37,32,8])
ultrasonesensor = ultrasonesensor(16)
kleurensensoren = kleurensensor([40, 38, 36, 26], [22, 18])

print(kleurensensoren.get_data_full())

while True:
    print(str(ultrasonesensor.get_data()) + " cm")  
    time.sleep(0.4)
    motor1.drive(random.randint(0, 100))

GPIO.cleanup()


"""
We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give, never gonna give
(Give you up)
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
"""
import RPi.GPIO as GPIO
import time

def test_func():
    return 'funktioniert '
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)


## Licht dimmen
p1 = GPIO.PWM(11, 50)  # frequency=50Hz
p2 = GPIO.PWM(13, 50)
p3 = GPIO.PWM(15, 50)
p4 = GPIO.PWM(40, 50)

#f=p1
f=p2
#f=p3
#f=p4

f.start(0)

try:
    while 1:
        for dc in range(0, 101, 5):
            f.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            f.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
    f.stop()
    GPIO.cleanup()






## Pins  11 rot , 13 blau , 15 grün, 40 pink

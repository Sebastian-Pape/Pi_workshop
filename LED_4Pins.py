import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(37, GPIO.OUT) # rot
#GPIO.setup(13, GPIO.OUT) # blau
#GPIO.setup(15, GPIO.OUT) # grün
#GPIO.setup(40, GPIO.OUT) # pink

def PWM(f, dc):
    p = GPIO.PWM(37, f)
    p.start(dc)
    for i in range(1, 100):
        p.ChangeDutyCycle(i)
        sleep(0.05)
    p.stop()

def all_on():
    GPIO.output(37, GPIO.HIGH)
    #GPIO.output(13, GPIO.HIGH)
    #GPIO.output(15, GPIO.HIGH)
    #GPIO.output(40, GPIO.HIGH)
    sleep(3)
    GPIO.output(37, GPIO.LOW)
    #GPIO.output(13, GPIO.LOW)
    #GPIO.output(15, GPIO.LOW)
    #GPIO.output(40, GPIO.LOW)

all_on()
PWM(100, 1)
GPIO.cleanup()

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# 11, 13, 15
GPIO.setup(11, GPIO.OUT) # rot
GPIO.setup(13, GPIO.OUT) # blau
GPIO.setup(15, GPIO.OUT) # grün
GPIO.setup(40, GPIO.OUT) # pink

def all_on():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(40, GPIO.HIGH)
    sleep(6)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(40, GPIO.LOW)

all_on()
GPIO.cleanup()

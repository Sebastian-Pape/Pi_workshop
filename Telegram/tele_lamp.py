import RPi.GPIO as GPIO
from time import sleep

def lamp_Strobo_20():
    for i in range(20):
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(36, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.LOW)
        sleep(0.1)

def lamp_Strobo():
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(36, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.LOW)
        sleep(0.1)

def lamp_gruen():
    GPIO.setup(38, GPIO.OUT)
    if GPIO.input(38):
        GPIO.output(38, GPIO.LOW)
    else:
        GPIO.output(38, GPIO.HIGH)

def lamp_blau():
    GPIO.setup(40, GPIO.OUT)
    if GPIO.input(40):
        GPIO.output(40, GPIO.LOW)
    else:
        GPIO.output(40, GPIO.HIGH)

def lamp_rot():
    GPIO.setup(36, GPIO.OUT)
    if GPIO.input(36):
        GPIO.output(36, GPIO.LOW)
    else:
        GPIO.output(36, GPIO.HIGH)

def lamp_off():
    GPIO.cleanup()

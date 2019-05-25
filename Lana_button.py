import RPi.GPIO as GPIO
from time import sleep

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.IN)
    GPIO.setup(40, GPIO.OUT)

def loop():
    while True:
        if GPIO.input(7):
            GPIO.output(40, GPIO.LOW)
        else:
            GPIO.output(40, GPIO.HIGH)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

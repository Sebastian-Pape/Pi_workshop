import RPi.GPIO as GPIO
from time import sleep

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.IN)
    GPIO.setup(35, GPIO.OUT)

def loop():
    while True:
        if GPIO.input(37):
            GPIO.output(35, GPIO.HIGH)
        else:
            GPIO.output(35, GPIO.LOW)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

try:
    import RPi.GPIO as GPIO
    on_pi = True
except:
    print('Not on api')
    on_pi = False
import time

if on_pi:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    light1 = GPIO.PWM(7, 50)  # frequency=50Hz

def cleanup():
    if on_pi:
        GPIO.cleanup()

def set_light_level(level):
    if on_pi:
        light1.ChangeDutyCycle(level)
    else:
        print('Setting light level to', level)

def light_on():
    if on_pi:
        light1.start(0)
        for percent in range(0, 101, 5):
            set_light_level(percent)
            time.sleep(0.1)
    else:
        print('turning light on')

def light_off():
    if on_pi:
        light1.start(100)
        for percent in range(100, -1, -5):
            set_light_level(percent)
            time.sleep(0.1)
    else:
        print('turning light off')

def aus():
    if on_pi:
        GPIO.output(7, GPIO.LOW)
    else:
        print('not connected')
    return 0

def an():
    if on_pi:
        GPIO.output(7, GPIO.HIGH)
    else:
        print('not connected')

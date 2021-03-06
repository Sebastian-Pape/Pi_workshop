#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import numpy as np

TRIG = 11
ECHO = 12

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

def distance():
	GPIO.output(TRIG, 0)
	time.sleep(0.000002)

	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)


	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	return during * 340 / 2 * 100

def loop():
	a = []
	for i in range(50):
		dis = distance()
		a.append(dis)
		print ''
		time.sleep(0.3)
	a = np.array(a)
	np.savetxt('data.txt', a)
def destroy():
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()

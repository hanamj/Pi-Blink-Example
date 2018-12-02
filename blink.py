import RPi.GPIO as GPIO
from time import sleep
import sys

# CONSTANTS   
LEDPIN = 4
ledOn = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT)

try:
	while True:
		GPIO.output(LEDPIN, ledOn)
		print "LED: " + str(ledOn)
		ledOn = not ledOn
	        sleep(0.5)

except KeyboardInterrupt:
	print 'Interrupted, cleaning GPIO!'
	GPIO.cleanup()
	sys.exit(0)

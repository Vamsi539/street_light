import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
while True:
    if(GPIO.input(11)==1):
        GPIO.output(13,True)
	time.sleep(1)
	GPIO.output(13,False)
	GPIO.output(16,False)
	GPIO.output(15,True)
	time.sleep(1)
	GPIO.output(13,False)
	GPIO.output(15,False)
	GPIO.output(16,True)
	time.sleep(1)
        print"Vehicle Detected"
	time.sleep(1)
	GPIO.output(16,False)
    else:
        GPIO.output(13,False)
	GPIO.output(15,False)
	GPIO.output(16,False)
        print"No Vehicle Detected"
	time.sleep(1)
GPIO.cleanup()

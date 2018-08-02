import json
import urllib2
import RPi.GPIO as GPIO
import time

def check(dvc_id):
	url="http://192.168.43.201/emilia-server/index.php/device/?dvc_id="+dvc_id
	json_obj=urllib2.urlopen(url)
	data = json.load(json_obj)
	return int(data['result'][0]['dvc_status'])

def lock():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)

        p = GPIO.PWM(7,50)
        p.start(7.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(11)
        time.sleep(1)
        p.stop()
        GPIO.cleanup()
	print('close')

def unlock():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)

        p = GPIO.PWM(7,50)
        p.start(7.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.stop()
        GPIO.cleanup()
	print('open')

dvc_id="ue025"
c_status=0
lock()
try:
	while True:
		s_status=check(dvc_id)
		if (c_status==0 and s_status==1):
			unlock()
			c_status=1
		if (c_status==1 and s_status==0):
			lock()
			c_status=0
		time.sleep(1)		
except KeyboardInterrupt:
	pass

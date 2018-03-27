import json
import urllib2
import time

def check(dvc_id):
	url="http://127.0.0.1/emilia-server/index.php/device/?dvc_id="+dvc_id
	json_obj=urllib2.urlopen(url)
	data = json.load(json_obj)
	return int(data[0]['dvc_status'])

def unlock():
	print('open')

def lock():
	print('close')

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
except KeyboardInterupt:
	pass

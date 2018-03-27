import json
import urllib2

url="http://127.0.0.1/emilia-server/index.php/nugen"
json_obj=urllib2.urlopen(url)
data = json.load(json_obj)
try:
	while True:
		for item in data:
			print item['dvc_id']
except KeyboardInterupt:
	pass
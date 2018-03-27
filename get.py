import json
import urllib2

url="http://127.0.0.1/emilia-server/index.php/device/?dvc_id=ue025"
json_obj=urllib2.urlopen(url)
data = json.load(json_obj)
print data[0]['dvc_status']
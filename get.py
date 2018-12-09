import json
import urllib
import urllib2

datan = {
    'action': 'sc_check',
    'dvc_id': 'bk803'
}
r=urllib2.urlopen('http://127.0.0.1/emilia-server/index.php/memberdeviceman', urllib.urlencode(datan))
data = json.load(r)
print(data['result']['status'])
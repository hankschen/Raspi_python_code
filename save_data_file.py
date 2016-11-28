#!/usr/bin/env python
# -*- coding=UTF-8 -*-
import urllib2
import json
import math
from time import sleep
READ_API_KEY = "UG1QRHRYGLSZVP8I"
CHANNEL_ID = "178323"

def main():
    f = open('db_file', 'w+')
    while True:
        conn = urllib2.urlopen("https://api.thingspeak.com/channels/%s/feed.json?api_key=%s" % (CHANNEL_ID,READ_API_KEY))
        response = conn.read()
        print "http status code = %s" %(conn.getcode())
        data = json.loads(response)
        print data
        f.write(str(data))
        conn.close()
        sleep(5)
if __name__=='__main__':
    main()


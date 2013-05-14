#!/usr/bin/env python
import urllib
import json
import sys

count = 0
while True:
	termFile = open(sys.argv[1])
	for line in termFile:
		response = urllib.urlopen("http://search.twitter.com/search.json?q="+line)
		data = json.load(response)
		count +=1	
	
		print data
		sys.stderr.write("\rDownloaded: " + str(count))
		
	sys.stdout.flush()		
	termFile.close()	

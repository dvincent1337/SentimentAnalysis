#!/usr/bin/env python
import urllib
import json
import sys

def printUsage():
	print ""
	output = "USAGE [TERM-FILE]"
	print output
	print ""
	output = "\tTERM-FILE - text file containing terms to rank, one per line"
	print output
	print ""
	print "\tNOTE: This program sends data to stdout, and status to stderr"
	print "\tNOTE: The data is in ast format!"
	print ""

def main():
	if len(sys.argv)<2:
		printUsage()
		return
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
if __name__ == '__main__':
	main()

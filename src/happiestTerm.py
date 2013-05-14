#!/usr/bin/env python
#Author David Vincent
#Permission to distribute and modify as desired is granted as long as following requirements are met:
#	Document changes made
#	Document name of authors
import re
import sys
import ast
import json
#global var decleartions:
scoreDict = {} 	#hold each word and it's sentiment score, format: {"Term": score}.
termDict = {}	#hold each term and score, format: {"Term":[score,count]}
termDictAverage = {}	#holds the average score of each term
maxTerms = 0		#(OPTIONAL) holds the maximim number of sentiments per term (if > 0)
def populateDicts():
	#populate the score dict
	inputFile = open(sys.argv[1])
	for line in inputFile:
		term, score = line.split("\t")
		scoreDict[term] = int(score)
	#populate the term dict
	inputFile.close()
	inputFile = open(sys.argv[2])
	for line in inputFile:
		line = line.rstrip()
		termDict[line] = [0.0,0]
		termDictAverage[line] = 0.0
	inputFile.close()

def isIn(word, string,ignoreCase=True):
	#test if word is in string.
	if ignoreCase:
		words = re.split("\W", string.lower() )
	else:
		words = re.split("\W",string)

	for text in words:
		if ignoreCase:
			if word.lower() == text:
				return True
		else:
			if word == text:
				return true
	return False
def calculateScore(string):
	#Calculates the score of sentiment
	#Assumes that scoreDict is populated
	score = 0.0;
	for word in re.split("\W", string.lower()):
		try:
			score += scoreDict[word]
		except:
			pass	
	return score
def performWork():
	tweetFile = open(sys.argv[3])
	count = 0	#number of states processed
	termCount = 0	#number of terms found in data
	
	#handle the maxTerms
	try:
		maxTerms = int(sys.argv[4])
	except:
		maxTerms = 0	
	#loop throuh each line in the tweet file:
	#  extract tweet, calculate sentiments
	for line in tweetFile:
		
		#end early if each terms is at max value
		if maxTerms > 0:
			keepGoingCount  = 0
			for item in termDict.keys():
				if termDict[item][1] >= maxTerms:
					keepGoingCount +=1
			if keepGoingCount == len(termDict.keys()):
				break;
			
		#Load the data from the line, try ast format, if that fails, try json.
		try:
			data = ast.literal_eval(line)
		except:
			try: 
				data = json.loads(line)
			except:
				#Through line of data if it can't be loaded.
				continue

		#Extract the data from the line
		if type(data) is dict:
			if not data.has_key(u'results'):
				continue
			if data[u'results']:
				for item in data[u'results']:
					tweetScore = calculateScore(item[u'text'])
					count += 1
					
					output = "Processing Item [" + str(count) + "]..."
					sys.stdout.write ("\r" +output)
					
					#don't update score for values that are zero
					if tweetScore != 0:
						for term in termDict.keys():
							#handle the maxTerms
							if maxTerms > 0 and termDict[term][1] >= maxTerms:
								continue
							#test to see if each term is in the tweet.
							if isIn(term,item[u'text']):
								#update the values:
								termCount +=1
								termDict[term][0] += tweetScore
								termDict[term][1] += 1
								termDictAverage[term] = (
									termDict[term][0]/termDict[term][1])
	#After looping through data, print results
	#Results printed from highest to lowest average score.
	print ""
	print "Terms\tScore\tCount\tPercentCount"
	print "**************************************"
	for term in sorted(termDictAverage, key=termDictAverage.get, reverse=True):
		output = term + "\t" + str(round(termDictAverage[term],4)) + "\t" + str(termDict[term][1])
		output += "\t" + str(round(100*termDict[term][1]/termCount,5))
		print output

def printUsage():
	print ""
	output = "USAGE: " + sys.argv[0] + " [SENTIMENT-FILE] [TERM-FILE] [TERM-DATA] {optional: MAXTERMS}"
	print output
	print ""
	output = "\tSENTIMENT-FILE - text file contaning pairs of tab seperated sentiments and values on each line"
	print output
	output = "\tTERM-FILE - text file containing terms to rank, one per line"
	print output
	output = "\tTERM-DATA - text file containing the data from twitter (in json format, or ast format)"
	print output
	output = "\tMAXTERMS - an integer value of the maximim amount of sentiments to calculate per term"
	print output
	print ""
def main():
	if len(sys.argv) < 4:
		printUsage()
		return	
	#hide cursor (linux):
	sys.stdout.write("\033[?25l")
	sys.stdout.flush()
	
	populateDicts()
	performWork()
	
	#show cousor(linux):
	sys.stdout.write("\033[?25h")
	sys.stdout.flush()

if __name__ == '__main__':
	main()

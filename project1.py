import os
import csv
import sys
import datetime


#print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#print (sys.argv[1])
try:
	#filename = r"file\sample.csv"
	#filename  = open('file\sample.csv', "rt", encoding="ascii")
	filename = open('file\sample.csv', "rt")
	#with open(filename, 'rb') as f:
	reader = csv.reader(filename) #read CSV FILE
	for csvRow in reader:
				recordID	= csvRow[0].strip()
				print(recordID)

except:
	raise


#print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
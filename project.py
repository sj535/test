import os
import csv
import sys
import DateTime

import matplotlib.pyplot as plt
import numpy as np

#a = list(range(0, 10))

try:
	filename = open('file\sample1.csv', "rt")
	reader = csv.reader(filename) #read CSV FILE
	csvRowCount	 = 0;
	csvColCount = 0;
	arrData = {}
	
	for csvRow in reader:
				csvRowCount	= csvRowCount+1
				#if(csvRowCount == 1):
				arrData['headerData'] = {}
				arrData['headerData'] = csvRow[0]
									
				for data in csvRow:
					print(data)
					if(csvRowCount <= 2):
						continue
					#arrData['data'] = csvRow
					#print(csvRowCount)
					"""if(data == ""):
						continue"""
					#print(csvRowCount)
					
					
					#print(data)
				#recordID	= csvRow[0].strip()
				#if recordID == "": #if no data found
				#	continue
				#print(recordID)
	
	print(arrData)
	
	
except:
	raise

	e = DateTime('US/Eastern')
	print(e.timezone())
#print DateTime.now().strftime("%Y-%m-%d %H:%M:%S")
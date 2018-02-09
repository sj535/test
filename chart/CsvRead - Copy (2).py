import os
import csv
import sys
import DateTime

import matplotlib.pyplot as plt
import numpy as np

#a = list(range(0, 10))

try:
	filename = '../file/sample1.csv'	
	csvRowCount	 = 0;
	csvColCount = 0;
	arrData = []	
	legendName = []
	xAxisName = []
	count = 0	
	dataArr = []
	data = {}	
	#f = open(filename)
	with open(filename, 'rt') as f:
		reader = csv.reader(f) #read CSV FILE
		for i in range(8): # count from 0 to 7
			row = reader
		#row = next(reader)
		print(row)
		exit()
		for row in data:
			print(row["Name"])
		#for csvRow in reader:
			#print(csvRow)
		
		exit()
		for arr in dataArr:
			print(arr)
		
	#		print(arr)
		#csvClm = csvRow[10]		
		exit()
		arrData1 = []
		if(arrData):
			#count1 = 0
			for key,dataVal in enumerate(arrData):
				#print(key)
				#print("\n\n")
				if(key >= 3):
					arrData1.append(dataVal)
		
		#print(xAxisName)
except:
	raise

	e = DateTime('US/Eastern')
	print(e.timezone())
#print DateTime.now().strftime("%Y-%m-%d %H:%M:%S")
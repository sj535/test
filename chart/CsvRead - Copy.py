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
	with open(filename, 'rt') as f:
		reader = csv.reader(f) #read CSV FILE
		#xAxisName.append(reader[2])		
		for csvRow in reader:				
			csvRowCount = csvRowCount + 1
			#print(csvRowCount)
			
			if csvRowCount < 2: # skip starting 2 blank line				
				continue
			if csvRowCount == 2: # skip header of file				
				xAxisName.append(csvRow[2])
				continue
			
			#csvRowCount	= csvRowCount+1
			csvClm = csvRow[10]
			
			
			
			#print(csvClm)
			#print("\n\n")		
			legendName.append(csvClm)			
			arrData.append(csvRow)
		
		
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
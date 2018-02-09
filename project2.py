import os
import csv
import sys
import DateTime

import matplotlib.pyplot as plt
import numpy as np

try:
	filename = open('file\sample.csv', "rt")
	reader = csv.reader(filename) #read CSV FILE
	csvRowCount	 = 0;
	csvColCount = 0;
	arrData = {}
	for csvRow in reader:
				csvRowCount	= csvRowCount+1
				#if(csvRowCount == 1):
				
				if(csvRowCount <= 2):
						continue					
				for data in csvRow:					
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
	
	
	t = np.arange(0.0, 2.0, 0.01)
	s = 1 + np.sin(2*np.pi*t)
	plt.plot(t, s)

	plt.xlabel('time (s)')
	plt.ylabel('voltage (mV)')
	plt.title('About as simple as it gets, folks')
	plt.grid(True)
	#plt.savefig("export_img/test.png")
	#plt.show()
	
except:
	raise

	e = DateTime('US/Eastern')
	print(e.timezone())
#print DateTime.now().strftime("%Y-%m-%d %H:%M:%S")
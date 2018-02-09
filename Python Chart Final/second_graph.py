import matplotlib.pyplot as plt 
import numpy as np  
import sys
import datetime
import CsvRead as CsvData #imported python file for CSV read 
import warnings
warnings.filterwarnings("ignore")

try:
	import ParamValidator as prmValid #validate parmas when run script from command line

	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

	ReadData = CsvData.readData() # read CSV data

	plt.rcParams["font.family"] = "Arial" # apply for whole chart

	now = datetime.datetime.now()
	curTime = now.strftime("%Y%m%d%H%M%S")

	saveFileNameParam = sys.argv[1] #Read first param save filename
	saveFileSizeParam = sys.argv[2] #Read first param for filesize
	savePath = "../export_img/" # Path to sace=
	saveFile = "_"+saveFileNameParam+".png"
	titleName = 'Operating Index \nEBIT Margin'
	color = ['#afdce3','#2e91ad','#91ccd1','#ff7800','#2e91ad'] #color code of line
	style = ['-','-','-','-',''] # line type
	marker = ['','','','o',''] # Marker type


	#legendLabel = ['75-Percentile','Median','25-Percentile','Hilti']
	legendLabel = ReadData['legendName'] # legend name
	markerSize = 5 # Marker width size
	lineWidthArr = [1,2,1,2,1] # Line width value
	lineWidth = 1.5  # Line width value
	count = 0 # Loop start count
	dottedKey = 3
	markerColor = '#ff6100' #marker color
	titleSize = 22
	numberFontSize = 15.5 #font size
	
	# Check if CSV file value is in percentage or not
	percentageExist = ReadData["perExist"]
	percentageFormat = '{:3.1f}'
	if percentageExist: percentageFormat = '{:3.1f}%'
		

	plt.figure(1)
	ax = plt.subplot(111)
	plt.subplots_adjust(bottom=0.2) # Plot size margin from Bottom
	ax.spines['right'].set_visible(False) #hide right line of chart
	ax.spines['left'].set_visible(False) #hide top line of chart

	x = np.array(list(range(len(ReadData['xAxisName']))))
	#x = [0,1,2,3,4,5,6,7,8,9]  # lines plot 	
	#y = [[-12.7,6.3,7.2,8.4,5.0,4.2,2.8,6.6,10.1],[-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8,4.6],[-21.2,-7.7,-4.2,0.5,-1.0,-1.6,-9.9,-1.0,3.4],[-18.2,2.2,1.7,5.2,3.2,3.6,-2.5,5.7,8.3]]
	yAxisValue = ReadData['axisValue']
	yAxisValue = [list(map(float, i)) for i in yAxisValue]
	y = np.array(yAxisValue)
	my_xticks = ReadData['xAxisName']

	#my_xticks = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17']

	plt.xticks(x, my_xticks,fontsize=numberFontSize)  #set X axis replace static number with original key value

	from scipy import interpolate # interpolate is used to convert the streight line with curve
	fillData = {}
	for data in y:
		#print(count)
		f = interpolate.interp1d(np.arange(len(data)), data, kind='cubic')
		xnew = np.arange(0, len(data)-1, 0.01)
		ynew = f(xnew)
		fillData[count] = f(xnew)	
		plt.plot(xnew, ynew, color=color[count],linestyle=style[count],markersize=markerSize,linewidth=lineWidthArr[count],label=legendLabel[count])  #Set plot final plot	
		count = count + 1

	# Fill color between two line start	
	fill1 = [0,1] #from y0 to y1
	fill2 = [1,2] #from y1 to y2
	colorFill = ['#afdce3','#91ccd1']
	count1 = 0
	for a,b in zip(fill1,fill2):
		plt.fill_between(xnew, fillData[a],fillData[b], color=colorFill[count1], alpha='1',interpolate=True) 
		count1 = count1 +1
	# Fill color between two line end
		
	plt.plot(y[dottedKey],color=markerColor,linestyle='',markersize=markerSize,linewidth=lineWidth,marker='o'); # first add orange marker without line	
	for i,j in zip(x,y[dottedKey]):	# added to display value on marker	
		ax.annotate(percentageFormat.format(j),xy=(i,j),horizontalalignment='right',verticalalignment='bottom',fontsize=numberFontSize)	#converted values into percentage value

	vals = ax.get_yticks()
	ax.set_yticklabels([percentageFormat.format(x) for x in vals],fontsize=numberFontSize) #converted values into percentage value
		
	plt.title(titleName,loc='left',fontsize=titleSize,fontweight="bold")

	fig = plt.gcf()
	if saveFileSizeParam == 'A4': #If A4 Size
		fig.set_size_inches(8.3, 11.7)
	elif saveFileSizeParam == 'A3': #If A3 Size
		fig.set_size_inches(11.7, 16.5)
	else: #Default fize size landscape
		fig.set_size_inches(10.5, 5.5)	
		
	plt.savefig(savePath+curTime+saveFile, dpi=300) #save image
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	#plt.show()
except Exception as e:	
	print("Something Went wrong! Unable to process your request.")
#	print(e)
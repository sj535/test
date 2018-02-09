import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import CsvRead as CsvData #imported python file for CSV read 
import sys
import warnings
warnings.filterwarnings("ignore")

try:
	import ParamValidator as prmValid #validate parmas when run script from command line

	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

	ReadData = CsvData.readData() # read CSV data

	plt.rcParams["font.family"] = "Arial" # apply for whole chart

	now = datetime.datetime.now()
	curTime = now.strftime("%Y%m%d%H%M%S")

		
	saveFileNameParam = sys.argv[1] #Read first param
	saveFileSizeParam = sys.argv[2]
	markerSize = 8 # Marker width size
	lineWidth = 2 # Line width value
	count = 0 # Loop start count
	dottedKey = 3 # define where we need a dotted key on which line
	titleName = 'Sales Growth'
	replaceCountWord = 'Count'
	savePath = "export_img/"
	saveFile = "_"+saveFileNameParam+".png"
	color = ['#2e91ad','#2e91ad','#2e91ad','#ff7800','#2e91ad'] #color code of line
	style = ['--','-','--','-',''] # line type
	marker = ['','','','o',''] # Marker type
	#legendLabel = ['Hilti','75-Percentile','Median','25-Percentile','count'] # legend name
	legendLabel = ReadData['legendName'] # legend name
	legendLabel1 = ReadData['legendName'] # legend name
	legendLabel1 = [w.replace(replaceCountWord, '_nolegend_') for w in legendLabel1] # replace Count word with _nolegend_. not required to display Count in legend
	#legendLabel1 = ['25-Percentile','Median','75-Percentile','Hilti','_nolegend_'] # legend name
	numberFontSize = 15.5


	# Check if CSV file value is in percentage or not
	percentageExist = ReadData["perExist"]
	percentageFormat = '{:3.1f}'
	if percentageExist: percentageFormat = '{:3.1f}%'


	# -- Start Plot  --
	plt.figure(1)
	ax = plt.subplot(111)
	plt.subplots_adjust(left=0.200,right = 0.8,bottom=0.3,wspace = 0.1,hspace = 0.1) # Plot size margin from Bottom #wspace = 0.1,hspace = 0.1
	ax.spines['right'].set_visible(False) #hide right line of chart
	ax.spines['top'].set_visible(False) #hide top line of chart

	x = np.array(list(range(len(ReadData['xAxisName']))))
	#x = np.array([0,1,2,3,4,5,6,7,8,9]) # set default x axis range 
	#y = np.array([[-18.2,2.2,1.7,5.2,3.2,3.6,-2.5,5.7,8.3],[-21.2,-7.7,-4.2,0.5,-1.0,-1.6,-9.9,-1.0,3.4],[-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8,4.6],[-12.7,6.3,7.2,8.4,5.0,4.2,2.8,6.6,10.1]]) # set parameter value
	yAxisValue = ReadData['axisValue']
	yAxisValue = [list(map(float, i)) for i in yAxisValue]
	#yAxisValue = [item.replace("%", "") for item in yAxisValue]
	y = np.array(yAxisValue)
	my_xticks = ReadData['xAxisName']

	#my_xticks = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17'] #set X axis value

	#plt.xticks(x, my_xticks,fontsize=15)  #set X axis replace static number with original key value
	for i,j in zip(x,y[dottedKey]):	# added to display value on marker		
		ax.annotate(percentageFormat.format(j),xy=(i,j),horizontalalignment='right',verticalalignment='bottom',fontsize=numberFontSize)	#converted values into percentage value	
	# If Percentage value exist start	
		
	from scipy import interpolate # interpolate is used to convert the streight line with curve
	legend_elements = []
	for data in y:
		# to set a curve line instead of streight line Start
		f = interpolate.interp1d(np.arange(len(data)), data, kind='cubic')
		xnew = np.arange(0, len(data)-1, 0.01)
		ynew = f(xnew)	
		# to set a curve line instead of streight line End
		plt.plot(xnew, ynew, color=color[count],linestyle=style[count],markersize=markerSize,linewidth=lineWidth,label=legendLabel[count]) #Set plot final plot
		legend_elements.append(Line2D([0], [0],color=color[count],label=legendLabel1[count],linestyle=style[count],markersize=markerSize,linewidth=lineWidth,marker=marker[count])) #to set the legend
		#ax.set_yticks([-25.0,-20.0,-15.0,-10.0,-05.0,-25.0,0.0,5.0,10.0,15.0])		
		#ax.set_ylim([-25,15])	
		count = count+1 # Auto increament of loop

	plt.plot(y[dottedKey],color='#ff6100',linestyle='',markersize=markerSize,linewidth=lineWidth,marker='o'); # first add orange marker without line
	ax.legend(handles=legend_elements,bbox_to_anchor=(1, 0.8),prop={'size': numberFontSize,'weight':'bold'},labelspacing=2,frameon=False) # to set the legend
	vals = ax.get_yticks()
	ax.set_yticklabels([percentageFormat.format(x) for x in vals],fontsize=15) #converted values into percentage value fontsize=15

	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])	
	"""
	k2 = []
	for k in y:	# added to display value on marker		
		for k1 in k:
			k2.append(percentageFormat.format(k1))	
	"""
	the_table = plt.table(cellText=y,rowLabels=legendLabel,colLabels=my_xticks,loc='bottom')
	the_table.set_fontsize(numberFontSize)
	the_table.scale(1,1.2)

	plt.xticks([])	
	plt.title(titleName,loc='left',fontsize=22,fontweight="bold")	#fontweight="bold"
	fig = plt.gcf()

	if saveFileSizeParam == 'A4': #If A4 Size
		fig.set_size_inches(8.3, 11.7)
	elif saveFileSizeParam == 'A3': #If A3 Size
		fig.set_size_inches(11.7, 16.5)
	else: #Default fize size landscape
		fig.set_size_inches(10.5, 5.5)	
	plt.savefig(savePath+curTime+saveFile) #save image
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	#plt.show()
except Exception as inst:	
	print("Something Went wrong! Unable to process your request.")
	print(inst)

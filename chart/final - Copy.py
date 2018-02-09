import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import CsvRead as CsvData

ReadData = CsvData.readData()

#exit()
plt.rcParams["font.family"] = "Arial" # apply for whole chart

now = datetime.datetime.now()
curTime = now.strftime("%Y%m%d%H%M%S")

markerSize = 8 # Marker width size
lineWidth = 2 # Line width value
count = 0 # Loop start count
dottedKey = 3 # define where we need a dotted key on which line
titleName = 'Sales Growth'
savePath = "../export_img/"
saveFile = "final_310118.png"
color = ['#2e91ad','#2e91ad','#2e91ad','#ff7800','#2e91ad'] #color code of line
style = ['--','-','--','-',''] # line type
marker = ['','','','','o',''] # Marker type
legendLabel = ['Hilti','75-Percentile','Median','25-Percentile','count'] # legend name
#legendLabel = ReadData['legendName'] # legend name
#legendLabel1 = ['Hilti','75-Percentile','Median','25-Percentile','_nolegend_'] # legend name
numberFontSize = 15.5

plt.figure(1)
ax = plt.subplot(111)
plt.subplots_adjust(bottom=0.3) # Plot size margin from Bottom
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
#my_xticks = ['2008\n\n9.0%\n-0.6%\n3.9%\n0.7%\n29%','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17']

#plt.xticks(x, my_xticks,fontsize=15)  #set X axis replace static number with original key value
for i,j in zip(x,y[dottedKey]):	# added to display value on marker	
	ax.annotate('{:3.1f}%'.format(j),xy=(i,j),horizontalalignment='right',verticalalignment='bottom',fontsize=numberFontSize)	#converted values into percentage value
from scipy import interpolate # interpolate is used to convert the streight line with curve
legend_elements = []
for data in y:
	# to set a curve line instead of streight line Start
	f = interpolate.interp1d(np.arange(len(data)), data, kind='cubic')
	xnew = np.arange(0, len(data)-1, 0.01)
	ynew = f(xnew)	
	# to set a curve line instead of streight line End
	plt.plot(xnew, ynew, color=color[count],linestyle=style[count],markersize=markerSize,linewidth=lineWidth,label=legendLabel[count]) #Set plot final plot
	legend_elements.append(Line2D([0], [0],color=color[count],label=legendLabel[count],linestyle=style[count],markersize=markerSize,linewidth=lineWidth,marker=marker[count])) #to set the legend
	#ax.set_yticks([-25.0,-20.0,-15.0,-10.0,-05.0,-25.0,0.0,5.0,10.0,15.0])		
	#ax.set_ylim([-25,15])	
	count = count+1 # Auto increament of loop

plt.plot(y[dottedKey],color='#ff6100',linestyle='',markersize=markerSize,linewidth=lineWidth,marker='o'); # first add orange marker without line
ax.legend(handles=legend_elements,bbox_to_anchor=(1, 0.8),prop={'size': numberFontSize,'weight':'bold'},labelspacing=2,frameon=False) # to set the legend
vals = ax.get_yticks()
ax.set_yticklabels(['{:3.1f}%'.format(x) for x in vals],fontsize=15) #converted values into percentage value fontsize=15

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])	

the_table = plt.table(cellText=y,rowLabels=legendLabel,colLabels=my_xticks,loc='bottom')
the_table.set_fontsize(numberFontSize)
the_table.scale(1,1.2)

plt.xticks([])	
plt.title(titleName,loc='left',fontsize=22,fontweight="bold")	#fontweight="bold"
fig = plt.gcf()
fig.set_size_inches(10.5, 5.5)
#plt.savefig(savePath+curTime+saveFile,dpi=100) #save image
plt.show()
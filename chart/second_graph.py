import matplotlib.pyplot as plt 
import numpy as np  
import sys
import warnings
import datetime
warnings.filterwarnings("ignore")


now = datetime.datetime.now()
curTime = now.strftime("%Y%m%d%H%M%S")

savePath = "export_img/"
saveFile = "_secondGraph.png"

plt.figure(1)
ax = plt.subplot(111)
plt.subplots_adjust(bottom=0.2) # Plot size margin from Bottom
ax.spines['right'].set_visible(False) #hide right line of chart
ax.spines['left'].set_visible(False) #hide top line of chart

titleName = 'Operating Index \nEBIT Margin'
x = [0,1,2,3,4,5,6,7,8,9]  # lines plot 
#y = [[-0.7,-0.5,4.9,2.6,2.2,1.1,1.9,2.2,2.8,3.4],[-1.7,-2.6,0.3,0.8,0.2,0.4,0.9,-0.2,1.4,1.8],[-4.2,-3.8,-0.5,-1.0,-0.2,-0.7,-0.3,-0.9,0.1,0.5],[-4.2,-3.8,-0.5,-1.0,-0.2,-0.7,-0.3,-0.9,0.1,0.5]]
y = [[-12.7,6.3,7.2,8.4,5.0,4.2,2.8,6.6,10.1],[-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8,4.6],[-21.2,-7.7,-4.2,0.5,-1.0,-1.6,-9.9,-1.0,3.4],[-18.2,2.2,1.7,5.2,3.2,3.6,-2.5,5.7,8.3]]
my_xticks = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17']

color = ['#afdce3','#2e91ad','#91ccd1','#ff7800'] #000000 
style = ['-','-','-','-']
marker = ['o','','','']
legendLabel = ['75-Percentile','Median','25-Percentile','Hilti']
markerSize = 5 # Marker width size
lineWidthArr = [1,2,1,2] # Line width value
lineWidth = 3
count = 0 # Loop start count
dottedKey = 3
plt.xticks(x, my_xticks,fontsize=12)  #set X axis replace static number with original key value

from scipy import interpolate # interpolate is used to convert the streight line with curve
fillData = {}
for data in y:
	#print(count)
	f = interpolate.interp1d(np.arange(len(data)), data, kind='cubic')
	xnew = np.arange(0, len(data)-1, 0.01)
	ynew = f(xnew)
	fillData[count] = f(xnew)	
	plt.plot(xnew, ynew, color=color[count],linestyle=style[count],markersize=markerSize,linewidth=lineWidthArr[count],label=legendLabel[count])	
	count = count + 1


fill1 = [0,1]
fill2 = [1,2]
color1 = ['#afdce3','#91ccd1']
count1 = 0
for a,b in zip(fill1,fill2):
	plt.fill_between(xnew, fillData[a],fillData[b], color=color1[count1], alpha='1',interpolate=True) 
	count1 = count1 +1

plt.plot(y[dottedKey],color='#ff6100',linestyle='',markersize=markerSize,linewidth=lineWidth,marker='o'); # first add orange marker without line	
for i,j in zip(x,y[dottedKey]):	# added to display value on marker	
	ax.annotate(format(j),xy=(i,j),horizontalalignment='right',verticalalignment='bottom')	#converted values into percentage value

vals = ax.get_yticks()
ax.set_yticklabels(['{:3.1f}%'.format(x) for x in vals])
	
plt.title(titleName,loc='left',fontsize="16")	#fontweight="bold"	
plt.savefig(savePath+curTime+saveFile) #save image
#plt.show()
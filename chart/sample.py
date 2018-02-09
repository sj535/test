import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

plt.rcParams["font.family"] = "Arial" # apply for whole chart

now = datetime.datetime.now()
curTime = now.strftime("%Y%m%d%H%M%S")

markerSize = 8 # Marker width size
lineWidth = 2 # Line width value
count = 0 # Loop start count
dottedKey = 0 # define where we need a dotted key on which line
titleName = 'Sales Growth'
savePath = "../export_img/"
saveFile = "final_310118.png"
color = ['#ff7800','#2e91ad','#2e91ad','#2e91ad'] #color code of line
style = ['-','--','-','--'] # line type
marker = ['o','','',''] # Marker type
legendLabel = ['Hilti','75-Percentile','Median','25-Percentile'] # legend name
numberFontSize = 15.5

plt.figure(1)
ax = plt.subplot(111)
plt.subplots_adjust(bottom=0.3) # Plot size margin from Bottom
ax.spines['right'].set_visible(False) #hide right line of chart
ax.spines['top'].set_visible(False) #hide top line of chart

x = np.array([0,1,2,3,4,5,6,7,8,9]) # set default x axis range 
y = np.array([[-18.2,2.2,1.7,5.2,3.2,3.6,-2.5,5.7,8.3],[-21.2,-7.7,-4.2,0.5,-1.0,-1.6,-9.9,-1.0,3.4],[-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8,4.6],[-12.7,6.3,7.2,8.4,5.0,4.2,2.8,6.6,10.1]]) # set parameter value
my_xticks = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17'] #set X axis value
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
fig.set_size_inches(16.53, 11.69) #16.53,11.69 - A3size
#fig.set_size_inches(10.5, 5.5)
#rc('figure', figsize=(11.69,8.27))
plt.savefig(savePath+curTime+saveFile,dpi=100) #save image
plt.show()
#,color=color[count],linestyle=style[count],markersize=14,linewidth=2,label='test',marker=marker[count]
exit()
x = np.array([0,1,2,3])
y = np.array([10,21,11,18])
my_xticks = ['2008','2009','2010','2011']
plt.xticks(x, my_xticks)
plt.plot(x, y)
plt.legend()
#plt.plot(x, y)
plt.show()


exit()

"""
hl, = plt.plot(['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17'], [-9.0, -21.2, -7.7, -4.2, 0.5, -1.0,-1.6,-9.9,-1.0,3.4],'b-.')

def update_line(hl, new_data):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_data))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_data))
    plt.draw()

plt.show()	
exit()
"""

"""
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

exit()
"""

"""
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()

exit()

names = [2007, 2008]
values = [1, 10]

plt.figure(1, figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
"""


"""

fig1 = plt.figure(1)
plt.plot([0, 1, 2, 3, 4], [0, 1, 2, 3, 4], label="Test", color='g')
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16],  label="Other Test",  color='r')
plt.grid(True)

#fig1.savefig('Foo1.png')
# add plt.close() after you've saved the figure
plt.close()

fig2 = plt.figure(2)
plt.plot([0, 1, 2, 3, 4], [0, 5, 1, 9, 2], label="Test 2", color='g')
plt.plot([0, 1, 2, 3, 4], [0, 10, 50, 0, 10],  label="Other Test 2",  color='r')
plt.grid(True)

#fig2.savefig('Foo2.png')

plt.show()

"""

#r'2008',r'2009',r'2010',r'2011',r'FY12',r'FY13',r'FY14',r'FY15',r'FY16',r'9M17'



#plt.set_title('style: {!r}'.format(sty), color='C0')
#plt.plot([r'2007', r'2008', r'2009', r'2010'], [-25, 4, 9, 56],color='#2df1ff',linestyle=':',markersize=14,label='test')
#plt.plot([r'2007', r'2008', r'2009', r'2011'], [-20, 5, 14, 40],color='#2df1ff',linestyle='--',markerfacecolor='blue', markersize=12)
#x1,x2,y1,y2 = plt.axis()
#plt.axis((x1,x2,2008,2011))
plt.plot([r'2008',r'2009',r'2010',r'2011',r'FY12',r'FY13',r'FY14',r'FY15',r'FY16',r'9M17'], [-9.0, -21.2, -7.7, -4.2, 0.5, -1.0,-1.6,-9.9,-1.0,3.4],color='#00f2ff',linestyle='-',markersize=14,linewidth=2,label='test')
plt.plot([r'2008',r'2009',r'2010',r'2011',r'FY12',r'FY13',r'FY14',r'FY15',r'FY16',r'9M17'], [-10, 2, 24, 50],color='#00f2ff',linestyle='--',markersize=16,linewidth=2)
plt.plot([r'2008',r'2009',r'2010',r'2011',r'FY12',r'FY13',r'FY14',r'FY15',r'FY16',r'9M17'], [-10, 2, 4, 40],color='#00f2ff',markevery=100,linestyle='--',markersize=16,linewidth=2)
plt.plot([r'2008',r'2009',r'2010',r'2011',r'FY12',r'FY13',r'FY14',r'FY15',r'FY16',r'9M17'], [-20, 5, 14, 40],color='#ff6100', marker='o',linestyle='-', linewidth=2, markersize=6)

plt.title('Sales Growth')
#plt.legend(['A simple line'])

#plt.plot(x, y, color='green', linestyle='dashed', marker='o',
   #  markerfacecolor='blue', markersize=12)
#plt.colors(['#000'])
#plt.plot([250, 350, 400, 300])
"""plt.plot([250, 350, 400, 300])
plt.plot([150, 320, 300, 225])
plt.plot([150, 220, 400, 125])
plt.plot([100, 50, 200, 205])"""
#plt.ylabel('Test')
plt.show()



"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 10)
for i in range(1, 6):
    plt.plot(x, i * x + i, label='$y = {i}x + {i}$'.format(i=i))
plt.legend(loc='best')
plt.show()
"""
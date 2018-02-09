import numpy as np
import matplotlib.pyplot as plt


plt.figure(1)
ax = plt.subplot(111)
plt.subplots_adjust(bottom=0.2) # Plot size margin from Bottom

ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

x = [0,1,2,3,4,5,6,7,8,9]
#y = np.array([[-18.2,2.2,1.7,0,3.2,3.6,-2.5,5.7,8.3],[-21.2,-7.7,-4.2,0.5,-1.0,-1.6,-9.9,-1.0,3.4],[-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8,4.6]])
#y = np.array([[-9.0,-21.2,-7.7,-4.2,0.5,-1.0,-1.6,-9.9,-1.0],[-0.6,-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8],[3.9,-12.7,6.3,7.2,8.4,5.0,4.2,2.8,6.6]])
y = [[-0.7,-0.5,4.9,2.6,2.2,1.1,1.9,2.2,2.8,3.4],[-1.7,-2.6,0.3,0.8,0.2,0.4,0.9,-0.2,1.4,1.8],[-4.2,-3.8,-0.5,-1.0,-0.2,-0.7,-0.3,-0.9,0.1,0.5]]
#,[-1.7,-2.6,0.3,0.8,0.2,0.4,0.9,-0.2,1.4,1.8],[-4.2,-3.8,-0.5,-1.0,-0.2,-0.7,-0.3,-0.9,0.1,0.5]
#print(x)


#exit()
#my_xticks = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17'] #set X axis value

#plt.xticks(x, my_xticks,fontsize=12)  #set X axis replace static number with original key value


color = ['#afdce3','#2e91ad','#91ccd1'] #000000
style = ['-','-','-','--']
marker = ['o','','','']
legendLabel = ['75-Percentile','Median','25-Percentile']
markerSize = 8 # Marker width size
lineWidth = [43,3,43] # Line width value
count = 0 # Loop start count

from scipy import interpolate # interpolate is used to convert the streight line with curve
for data in y:
	# to set a curve line instead of streight line Start
	f = interpolate.interp1d(np.arange(len(data)), data, kind='cubic')
	xnew = np.arange(0, len(data)-1, 0.01)
	ynew = f(xnew)	
	# to set a curve line instead of streight line End
	plt.plot(xnew, ynew, color=color[count],linestyle=style[count],markersize=markerSize,linewidth=lineWidth[count],label=legendLabel[count]) #Set plot final plot
	count = count + 1

#y1 = np.array([[3.9,-12.7,6.3,7.2,8.4,5.0,4.2,2.8,6.6]])
#ax_c = ax.twinx()
#ax.legend()
#plt.plot(x,y1, color='blue', label='mortgage')
#plt.plot(y1,color='#ff6100',linestyle='',markersize=8,linewidth=3,marker='o'); # first add orange marker without line
#plt.stackplot(x, y,colors=color,labels=legendLabel)
#plt.plot(x, y,color=color,labels=legendLabel,style=style,marker=marker)

#, color=color,linestyle=style,markersize=8,linewidth=3,label=legendLabel
#ax.set_yticks([-25.0,-20.0,-15.0,-10.0,-05.0,-25.0,0.0,5.0,10.0,15.0])		


#plt.legend()

#,linestyle=style,labels=legendLabel
#for color1,style1,marker1,legendLabel1 in zip(color,style,marker,legendLabel):		
		
#ax.plot(x,y)

#ax_c.set_ylabel('Celsius')

plt.title('Operating Index EBIT Margin',loc='left',fontsize="15.5")	#fontweight="bold",

plt.show()

exit()


#my_xticks = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17']



def fnx():
    return np.random.randint(5, 50, 10)

y = np.row_stack((fnx(), fnx(), fnx()))

x = np.arange(10)

y1, y2, y3 = fnx(), fnx(), fnx()

fig, ax = plt.subplots()
ax.stackplot(x, y)
plt.show()

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3)
plt.show()







import matplotlib.pyplot as plt

months= [x for x in range(1,13)]

mortgage= [700, 700, 700,
           800, 800, 800,
           850, 850, 850,
           850, 850, 850]

utilities= [500, 300, 380,
           200, 600, 550,
           310, 620, 290,
           320, 440, 400]

repairs= [100, 120, 100,
          150, 850, 80,
          120, 220, 240,
          50, 60, 150]

plt.plot([],[], color='blue', label='mortgage')
plt.plot([],[], color='orange', label='utilities')
plt.plot([],[], color='brown', label='repairs')


plt.stackplot(months, mortgage, utilities, repairs, colors=['blue', 'orange', 'brown'])

plt.legend()

plt.title('Household Expenses')
plt.xlabel('Months of the year')
plt.ylabel('Cost')

plt.show()

exit()
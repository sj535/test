import matplotlib.pyplot as plt 
import numpy as np  



x = [0,1,2,3,4,5,6,7,8,9]  # lines plot 
y = [[-0.7,-0.5,4.9,2.6,2.2,1.1,1.9,2.2,2.8,3.4],[-1.7,-2.6,0.3,0.8,0.2,0.4,0.9,-0.2,1.4,1.8],[-4.2,-3.8,-0.5,-1.0,-0.2,-0.7,-0.3,-0.9,0.1,0.5]]
my_xticks = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17']
#y3 = [-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8,4.6]
# upper edge of polygon (min of lines y1 & y2) 
#y4 = np.minimum(y1, y2)  
# set y-limit, making neg y-values not show in plot 
#plt.ylim(0, 5)  
# plotting of lines 
color = ['#afdce3','#2e91ad','#91ccd1'] #000000
style = ['-','-','-','--']
marker = ['o','','','']
legendLabel = ['75-Percentile','Median','25-Percentile']
markerSize = 8 # Marker width size
lineWidth = [1,3,1] # Line width value
count = 0 # Loop start count
plt.xticks(x, my_xticks,fontsize=12)  #set X axis replace static number with original key value

from scipy import interpolate # interpolate is used to convert the streight line with curve

yLenCnt = len(y)-1
#print(yLenCnt)
#exit()

#plt.fill_between(x, y[1], y[2], color='#91ccd1', alpha='0.7',interpolate=True) 
#print(y[1])
#exit()
new = {}
for data in y:
	#print(count)
	f = interpolate.interp1d(np.arange(len(data)), data, kind='cubic')
	xnew = np.arange(0, len(data)-1, 0.01)
	ynew = f(xnew)
	new[count] = f(xnew)
	#print(new[count])
	#exit()
	#ynew + " " + count = f(xnew)
	#ynew1 = {}	
	#ynew1[count] = f(xnew)
	
	
	#print(ynew)
	#print('\n')	
	# to set a curve line instead of streight line End
	#plt.plot(xnew, ynew, color=color[count],linestyle=style[count],markersize=markerSize,linewidth=lineWidth[count],label=legendLabel[count]) #Set plot final plot
	plt.plot(xnew, ynew, color=color[count],linestyle=style[count],markersize=markerSize,linewidth=lineWidth[count],label=legendLabel[count])
	
	#if yLenCnt <= count:
	#print(count+1)
	print('\n')
	#if yLenCnt <= count:	
	
	#plt.fill_between(xnew, data[0], data[1], where=data[1] <= data[0], color='#afdce3', alpha='0.5', interpolate=True) 
	#plt.fill_between(xnew, data[0], data[1], where=data[1] >= data[0], color='#afdce3', alpha='0.5', interpolate=True) 
	#plt.fill_between(xnew, 0, 2, color='#afdce3', alpha='0.5', interpolate=True) 
	# plt.fill_between(xnew, ynew[0], ynew[1], color='#afdce3', alpha='0.5',interpolate=True) 
	#plt.fill_between(xnew, ynew[1], ynew[2], color='#91ccd1', alpha='0.7',interpolate=True)
	#if yLenCnt > count:  
		#print('--!')	
	#plt.fill_between(x, y[1], y[2], color='#91ccd1', alpha='0.7',interpolate=True) 
	#plt.fill_between(xnew, ynew, color=color[count], alpha='0.5',interpolate=True) 
	#plt.fill_between(x, data, color=color[count], alpha='0.5',interpolate=True) 
	count = count + 1


fill1 = [0,1]
fill2 = [1,2]
for a,b in zip(fill1,fill2):
	plt.fill_between(xnew, new[a],new[b], color='#afdce3', alpha='0.5',interpolate=True) 
	
#exit()
#print(ynew1)
#exit()
# filling between line y3 , line y4 
#plt.fill_between(x, y[0], y[1], color='#afdce3', alpha='0.5',interpolate=True) 
#plt.fill_between(x, y[1], y[2], color='#91ccd1', alpha='0.7',interpolate=True) 
plt.show()
exit()


x = [0,1,2,3,4,5,6,7,8]  # lines plot 
y1 = [-18.2,2.2,1.7,5.2,3.2,3.6,-2.5,5.7,8.3] 
y2 = [-21.2,-7.7,-4.2,0.5,-1.0,-1.6,-9.9,-1.0,3.4]
y3 = [-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8,4.6]
#y3 = [-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8,4.6]
# upper edge of polygon (min of lines y1 & y2) 
#y4 = np.minimum(y1, y2)  
# set y-limit, making neg y-values not show in plot 
#plt.ylim(0, 5)  
# plotting of lines 
color = ['#afdce3','#2e91ad','#91ccd1'] #000000
plt.plot(x, y1, x, y2, x,y3)
# filling between line y3 , line y4 
plt.fill_between(x, y1, y2, color='#afdce3', alpha='0.5') 
plt.fill_between(x, y2, y3, color='#91ccd1', alpha='0.5') 
plt.show()
exit()


x = np.arange(0,10,0.1)  # lines plot 
y1 = 4 - 2*x 
y2 = 3 - 0.5*x 
y3 = 1 -x  
# upper edge of polygon (min of lines y1 & y2) 
y4 = np.minimum(y1, y2)  
# set y-limit, making neg y-values not show in plot 
plt.ylim(0, 5)  
# plotting of lines 
plt.plot(x, y1,x,y2,x, y3)  
# filling between line y3 , line y4 
plt.fill_between(x, y3, y4, color='grey', alpha='0.5') 
plt.show()
exit()

import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,1,2,3,4,5,6,7,8])
y1 = [-18.2,2.2,1.7,5.2,3.2,3.6,-2.5,5.7,8.3]
#y2 = 1.2*np.sin(4*np.pi*x)

fig, (ax1) = plt.subplots(1, 1, sharex=True)
#ax1 = plt.subplots(1, 1, sharex=True)
ax1.fill_between(x, 0, y1)
ax1.set_ylabel('between y1 and 0')

ax1.set_yticks([-25.0,-20.0,-15.0,-10.0,-05.0,-25.0,0.0,5.0,10.0,15.0])


plt.show()

exit()

import matplotlib.pyplot as plt
import numpy as np

Nsteps, Nwalkers = 100, 250
t = np.arange(Nsteps)

# an (Nsteps x Nwalkers) array of random walk steps
S1 = 0.002 + 0.01*np.random.randn(Nsteps, Nwalkers)
S2 = 0.004 + 0.02*np.random.randn(Nsteps, Nwalkers)

# an (Nsteps x Nwalkers) array of random walker positions
X1 = S1.cumsum(axis=0)
X2 = S2.cumsum(axis=0)


# Nsteps length arrays empirical means and standard deviations of both
# populations over time
mu1 = X1.mean(axis=1)
sigma1 = X1.std(axis=1)
mu2 = X2.mean(axis=1)
sigma2 = X2.std(axis=1)

# plot it!
fig, ax = plt.subplots(1)
ax.plot(t, mu1, lw=2, label='mean population 1', color='blue')
ax.plot(t, mu2, lw=2, label='mean population 2', color='yellow')
ax.fill_between(t, mu1+sigma1, mu1-sigma1, facecolor='blue', alpha=0.5)
ax.fill_between(t, mu2+sigma2, mu2-sigma2, facecolor='yellow', alpha=0.5)
ax.set_title('random walkers empirical $\mu$ and $\pm \sigma$ interval')
ax.legend(loc='upper left')
ax.set_xlabel('num steps')
ax.set_ylabel('position')
ax.grid()
plt.show()

exit()

import numpy as np
import matplotlib.pyplot as plt


def fnx():
    return np.random.randint(5, 50, 10)

y = np.row_stack((fnx(), fnx(), fnx()))
x = np.arange(9)

#y1, y2, y3 = fnx(), fnx(), fnx()
#y1 = [7, 12, 39, 38, 10, 28, 12, 40, 14, 13]
#y2 = [25, 2, 19, 28, 15, 29, 16, 30, 4, 16]
y1 = [-18.2,2.2,1.7,0,3.2,3.6,-2.5,5.7,8.3]
#y2 = [-21.2,-7.7,-4.2,0.5,-1.0,-1.6,-9.9,-1.0,3.4]

#print(y1)
#exit()
#fig, ax = plt.subplots()
#ax.stackplot(x, y)
#plt.show()

fig, ax = plt.subplots()
ax.stackplot(x, y1)
plt.show()

exit()



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
my_xticks = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17'] #set X axis value

plt.xticks(x, my_xticks,fontsize=12)  #set X axis replace static number with original key value


color = ['#afdce3','#2e91ad','#91ccd1'] #91ccd1
style = ['-','--','-','--']
marker = ['o','','','']
legendLabel = ['75-Percentile','Median','25-Percentile']



#y1 = np.array([[3.9,-12.7,6.3,7.2,8.4,5.0,4.2,2.8,6.6]])
#ax_c = ax.twinx()
#ax.legend()
#plt.plot(x,y1, color='blue', label='mortgage')
#plt.plot(y1,color='#ff6100',linestyle='',markersize=8,linewidth=3,marker='o'); # first add orange marker without line
#plt.fill(x,y)
plt.stackplot(x, y,colors=color,labels=legendLabel)
#plt.plot(x, [-0.7,-0.5,4.9,2.6,2.2,1.1,1.9,2.2,2.8,3.4],color='#ff7800',labels='Median')
#plt.plot(x, y, color=color,linestyle=style,markersize=8,linewidth=3,label=legendLabel) #Set plot final plot
#ax.set_yticks([-25.0,-20.0,-15.0,-10.0,-05.0,-25.0,0.0,5.0,10.0,15.0])		


plt.legend()

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
import matplotlib.pyplot as plt
import re

some_list = [['10', 'def-456', 'ghi-789', 'abc-456'],['10', 'def-456%', 'ghi-789', 'abc-456']]
for list in some_list:
	if any("%" in s for s in list):
		print("dasd")

exit()
# data 
all_x = ["apple","10%","apple55"]
all_y = [[1,3], [1.5,2.9]]

search = ['%','orange', 'banana']

a = any(x in all_x for x in search)

#re.search("|".join(search), all_x)
print(a)
exit()

#print(all_y)
exit()
# Plot
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.plot(all_x, all_y)

# Add legend, title and axis labels
lgd = ax.legend( [ 'Lag ' + str(lag) for lag in all_x], loc='center right', bbox_to_anchor=(1.3, 0.5))
ax.set_title('Title')
ax.set_xlabel('x label')
ax.set_ylabel('y label')  
plt.show()

exit()

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
print(x)
fig = plt.figure()
ax = plt.subplot(111)

for i in range(5):
	print(i)
    #ax.plot(x, i * x, label='$y = %ix$' % i)
exit()
ax.legend()

plt.show()


exit()


import numpy as np
x = np.array([[ '0.42436315%', 0.48558583, 0.32924763], [ 0.7439979,0.58220701,0.38213418], [ 0.5097581,0.34528799,0.1563123 ]])
print("Original array:")
print(x)
print("Replace all elements of the said array with .5 which are greater than .5")
#x[x > .5] = .5

x = [w.replace('%', '_nolegend_') for w in x]
#x.replace("%","---")
print(x)


exit()


from matplotlib import pyplot
import numpy


a = numpy.array([[ 3.57,  1.76,  7.42,  6.52],
                 [ 1.57,  1.2 ,  3.02,  6.88],
                 [ 2.23,  4.86,  5.12,  2.81],
                 [ 4.48,  1.38,  2.14,  0.86],
                 [ 6.68,  1.72,  8.56,  3.23]])


def plotCollection(ax, xs, ys, *args, **kwargs):

  ax.plot(xs,ys, *args, **kwargs)

  if "label" in kwargs.keys():

    #remove duplicates
    handles, labels = pyplot.gca().get_legend_handles_labels()
    newLabels, newHandles = [], []
    for handle, label in zip(handles, labels):
      if label not in newLabels:
        newLabels.append(label)
        newHandles.append(handle)

    pyplot.legend(newHandles, newLabels)

ax = pyplot.subplot(1,1,1)  
plotCollection(ax, a[:,::2].T, a[:, 1::2].T, 'r', label='data_a')
plotCollection(ax, a[:,1::2].T, a[:, ::2].T, 'b', label='data_b')
pyplot.show()

exit()



import numpy as np
import matplotlib

import matplotlib.pyplot as plt

"""
x = [0,1,2,3,4,5,6,7,8,9]
y1 = [-0.7,-0.5,4.9,2.6,2.2,1.1,1.9,2.2,2.8,3.4]
y2 = [-1.7,-2.6,0.3,0.8,0.2,0.4,0.9,-0.2,1.4,1.8]

fig, (ax1) = plt.subplots(1, 1, sharex=True)

ax1.fill_between(x, 0, y1)
ax1.fill_between(x, y1, y2)
#ax1.fill_between(x, 0, y2)
ax1.set_ylabel('between y1 and 0')

plt.show()

exit()

"""

"""
#plt.xscale('log')

xs = np.array([10, 100])
ys = np.array([10, -25])
zeros = np.array([0, 0])



x_lots = np.linspace(10, 100, 512)
y_lots = np.linspace(10, -25, 512)
plt.plot(x_lots, y_lots)

plt.fill_between(xs, zeros, ys, where=ys > zeros, facecolor='green', interpolate=True, alpha=.5)
plt.fill_between(xs, zeros, ys, where=ys < zeros, facecolor='red', interpolate=True, alpha=.5)

plt.fill_between(x_lots, 0, y_lots, where=y_lots > 0, facecolor='green', interpolate=True, alpha=.5)
plt.fill_between(x_lots, 0, y_lots, where=y_lots < 0, facecolor='red', interpolate=True, alpha=.5)


plt.show()

exit()
"""

fig=plt.figure()
ax=fig.add_subplot(111)

x = [0,1,2,3,4,5,6,7,8,9]  # lines plot 
y1 = [-0.7,-0.5,4.9,2.6,2.2,1.1,1.9,2.2,2.8,3.4]
y2 = [-1.7,-2.6,0.3,0.8,0.2,0.4,0.9,-0.2,1.4,1.8]
y3 = [-4.2,-3.8,-0.5,-1.0,-0.2,-0.7,-0.3,-0.9,0.1,0.5]

#y1 = [-18.2,2.2,1.7,5.2,3.2,3.6,-2.5,5.7,8.3]
#y2 = [-21.2,-7.7,-4.2,0.5,-1.0,-1.6,-9.9,-1.0,3.4]
#y3 = [-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8,4.6]

my_xticks = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17']
plt.xticks(x, my_xticks,fontsize=12)  #set X axis replace static number with original key value
#y3 = [-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8,4.6]
# upper edge of polygon (min of lines y1 & y2) 
#y4 = np.minimum(y1, y2)  
# set y-limit, making neg y-values not show in plot 
#plt.ylim(0, 5)  
# plotting of lines 
color = ['#afdce3','#2e91ad','#91ccd1'] #000000

from scipy import interpolate
f = interpolate.interp1d(np.arange(len(y1)), y1, kind='cubic')
xnew = np.arange(0, len(y1)-1, 0.01)
ynew = f(xnew)	

f = interpolate.interp1d(np.arange(len(y2)), y2, kind='cubic')
xnew1 = np.arange(0, len(y2)-1, 0.01)
ynew1 = f(xnew1)

f = interpolate.interp1d(np.arange(len(y3)), y3, kind='cubic')
xnew2 = np.arange(0, len(y3)-1, 0.01)
ynew2 = f(xnew2)


plt.plot(xnew, ynew,linewidth='0',color='#afdce3')
plt.plot(xnew1, ynew1,linewidth='3',label='test',color='#2e91ad')
plt.plot(xnew2, ynew2,linewidth='0',color='#91ccd1')
# filling between line y3 , line y4 
plt.fill_between(xnew, ynew, ynew1, color='#afdce3', alpha='0.5',interpolate=True) 
plt.fill_between(xnew1, ynew1, ynew2, color='#91ccd1', alpha='0.7',interpolate=True) 

#ax.set_yticks([-25.0,-20.0,-15.0,-10.0,-05.0,-25.0,0.0,5.0,10.0,15.0])	
plt.show()
exit()

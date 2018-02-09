import matplotlib.pyplot as plt
import numpy as np
"""
#x = np.arange(1,10)
x = np.array([0,1,2,3,4,5,6,7,8,9])
y1 = x
y2 = x*2
y3 = x*3

lines = [y1,y2,y3]
colors  = ['r','g','b']
labels  = ['RED','GREEN','BLUE']
my_xticks = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17']
plt.xticks(x, my_xticks)
# fig1 = plt.figure()
for i,c,l,m in zip(lines,colors,labels,my_xticks): 	
    plt.plot(x,i,c,label='l')
	#plt.xticks(x, m)
    plt.legend(labels)    
plt.show()

exit()
"""
add_z = np.array([ 22.39409055, 20.91765398, 19.80805759, 19.14836638, 23.54310977, 19.68638808, 21.25143616, 21.32550146, 18.80392599, 17.37016759, 19.21143494, 18.27464661, 21.25150385, 20.61853909, 22.89028155, 22.3965408 ])
#add_z = np.array([0,1,2,3,4,5,6,7,8,9])
dataNew = np.array([[ 26.69], [ 24.94], [ 22.37], [ 23.5 ], [ 22.69], [ 22.62], [ 18.5 ], [ 20.87], [ 19. ], [ 19.75], [ 20.72], [ 19.78], [ 20.38], [ 22.06]])
#dataNew = np.array([0.7, -18.2, 2.2, 1.7, 5.2, 3.2,3.6,-2.5,5.7,8.3])

plt.figure(figsize = (10,5))
#plt.plot(dataNew[:],'g')
plt.plot(add_z[:],color='#ff6100',linestyle='',markersize=6,linewidth=2,label='test',marker='o');
#plt.plot(xnew, ynew, color='#ff6100',linestyle='',markersize=6,linewidth=2,label='test',marker='o')

from scipy import interpolate
f = interpolate.interp1d(np.arange(len(add_z)), add_z, kind='cubic')
xnew = np.arange(0, len(add_z)-1, 0.1)
ynew = f(xnew)
#plt.xticks(x, my_xticks)
plt.plot(xnew, ynew, color='#ff6100',linestyle='-')

plt.show()
exit()

"""
=================
Multiple subplots
=================

Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt
"""
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([77, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title

#plt.plot([1,2,3,4], [1,4,9,16])
#plt.axis([0, 6, 0, 20])
plt.show()
exit()
"""
x = np.linspace(0, 6, 100)
#print(x)
#exit()
x = np.array([0,7,5,15])
#print(x)
#exit()
#y_1 = [1.0,5,0.2,-1]
y_1 = 5*x
y_2 = np.power(x, 2)
y_3 = np.exp(x/1.5)
plt.plot(x, y_1)
plt.plot(x, y_2)
plt.plot(x, y_3)
plt.show()

exit()


x1 = np.linspace(0.0, 5.0)
#x2 = np.linspace(0.0, 2.0)
#x2 = np.array([0,7,5,15])
x2 = np.linspace(2.0, 3.0, num=4, retstep=False)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
#y2 = np.cos(2 * np.pi * x2)
y2 = [1.0, 5,0.2,-1]
#print(y2)
#exit()

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show()

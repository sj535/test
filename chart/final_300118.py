import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(num=None, figsize=(10, 7), dpi=80, facecolor='w', edgecolor='k')
ax = fig.add_subplot(111)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([[-21.2,-7.7,-4.2,0.5,-1.0,0,-9.9,-1.0,3.4],[-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8,4.6],[-12.7,6.3,7.2,8.4,5.0,4.2,2.8,6.6,10.1],[-18.2,2.2,1.7,5.2,3.2,3.6,-2.5,5.7,8.3]])
my_xticks = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17']
color = ['#ff6100','#00f2ff','#00f2ff','#00f2ff']
style = ['-','--','-','--']
marker = ['o','','','']
legendLabel = ['Hilti','75-Percentile','Median','25-Percentile']
count = 0
dottedKey = 0
plt.xticks(x, my_xticks)
plt.plot(y[dottedKey],color='#ff6100',linestyle='',markersize=6,linewidth=2,marker='o');
from scipy import interpolate
for data in y:
	f = interpolate.interp1d(np.arange(len(data)), data, kind='cubic')
	xnew = np.arange(0, len(data)-1, 0.01)
	ynew = f(xnew)	
	plt.plot(xnew, ynew, color=color[count],linestyle=style[count],markersize=6,linewidth=2,label=legendLabel[count])
	#ax.set_yticks([-25.0,-20.0,-15.0,-10.0,-05.0,-25.0,0.0,5.0,10.0,15.0])		
	#plt.legend()
	count = count+1

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])	
ax.legend(loc='center left',bbox_to_anchor=(1, 0.7),prop={'size': 14},labelspacing=4,frameon=False)
	
plt.title('Sales Growth',loc='left',fontsize="16")	#fontweight="bold",
plt.savefig("final_300118_1.png")
plt.show()
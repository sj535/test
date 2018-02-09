import numpy as np
import matplotlib.pyplot as plt

x=[2009,2010,2011,2012,2013,2014,2015,2016,2017]
y= [-18.2, 2.2,1.7,5.2,3.2,3.6,-2.5,5.7,8.3]
x1=[2009,2010,2011,2012,2013,2014,2015,2016,2017]
y1= [-17.7,-2.5,1.9,3.1,1.9,2.2,-4.7,3.8,4.6]
x2=[2009,2010,2011,2012,2013,2014,2015,2016,2017]
y2= [-21.2,-7.7,-4.2,0.5,-1.0,-1.6,-9.9,-1.0,3.4]

fig = plt.figure(num=None, figsize=(10, 7), dpi=80, facecolor='w', edgecolor='k')
ax = fig.add_subplot(111)
ax.set_ylim(0,10)
#ax.set_xlim(20,20)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#plt.plot(x,y)
for i,j in zip(x,y):	
    ax.annotate(str(j),xy=(i,j))

plt.axis([2009, 2017, -25.0, 15.0])

xsquad=['2009Y\n\nJan\nJan1\njan2','2010Y','2011Y','2012Y','2013Y','2014y','2015Y','2016Y','2017Y    test']
ysquad= ['-25.0%','-20.0%','-15.0%','-10.0%','-05.0%','-25.0%','0.0%','5.0%','10.0%','15.0%']
ax.set_xticks([2009,2010,2011,2012,2013,2014,2015,2016,2017])
ax.set_xticklabels(xsquad, minor=False)
ax.set_yticks([-25.0,-20.0,-15.0,-10.0,-05.0,-25.0,0.0,5.0,10.0,15.0])
ax.set_yticklabels(ysquad, minor=False)
ax.xaxis.set_tick_params(pad=-15)
xvals=[2009,2010,2011,2012,2013,2014,2015,2016,2017]
plt.xlim([min(xvals) - 0.5, max(xvals) + 0.5])
plt.plot([2009,2010,2011,2012,2013,2014,2015,2016,2017], [-12.7, 6.3,7.2,8.4,5.0,4.2,2.8,6.6,10.1], '--', color='#75bbfd',label='75-Percentile',)
plt.plot(x,y, '-', marker='o', color='#FFA500',label='hilti', linewidth=2,solid_joinstyle='round')
plt.plot(x1,y1, '-',color='#75bbfd',label='Median', linewidth=2,solid_joinstyle='round')
plt.plot(x2,y2, '--', color='#75bbfd',label='25-Percentile', linewidth=2,solid_joinstyle='round')



#plt.xlabel('Radius')
#plt.ylabel('Area')
#plt.title('Sales Groath')
plt.title('Sales Groath', loc='left')
#plt.grid(True)


# Now add the legend with some customizations.
legend = ax.legend(loc='center right', shadow=False)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
#frame = legend.get_frame()
#frame.set_facecolor('0.90')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('small')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

plt.show()

#plt.xticks([0.2, 0.4, 0.6, 0.8, 1.],
           #["Jan\n2009", "Feb\n2009", "Mar\n2009", "Apr\n2009", "May\n2009"])
###
#x = [0,5,9,10,15]
#y = [0,1,2,3,4]
#plt.plot(x,y)
#plt.xticks(np.arange(min(x), max(x)+1, 1.0))
###


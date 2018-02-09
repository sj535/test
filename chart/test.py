import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
 
# line 1 points
x1 = [1,2,3]
y1 = [2,4,1]
# plotting the line 1 points 
plt.plot(x1, y1, label = "line 1")
 
# line 2 points
x2 = [1,2,3]
y2 = [4,1,3] 
# plotting the line 2 points 
plt.plot(x2, y2, label = "line 2")
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()

"""


# x axis values
#x = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17']
x = [0,1,2,3,4,5,6,7,8,9]

# corresponding y axis values
y = [2,4,1,5,2,6,5,2,6,5]
#my_xticks = ['2008','2009','2010','2011','FY12','FY13','FY14','FY15','FY16','9M17','test'] 
# plotting the points 
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
 
#plt.xticks(x, my_xticks)
# setting x and y axis range
plt.ylim(1,10)
plt.xlim(1,10)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('Some cool customizations!')
 
# function to show the plot
plt.show()
"""

"""
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title
plt.show()
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111)


# initialize array with size number of lines
data = np.full((2,10), None) 

# fill data array with data points [x,y,z]
#data = [[[0,3],[0,0],[0,0]],[[0,3],[0.5,0.5],[0,0]]]
#data[0] = [[0,3],[0,0],[0,0]]
#data[1] = [[0,3],[0.5,0.5],[0,0]]
data = np.array([[[r'0',r'3',r'55',r'8'],[1,2,0,4],[5,6,7,8]],
                 #[[r'0',r'4'],[0.5,0.5],[0,0]],
                 #[[r'0',r'2'],[1,2],[3,0]]
				])
# etc...
#print(data)
#exit()
# loop over data array and plot lines
for line in data:
	#print(line[2])
    ax.plot(line[0],line[1],line[2])
	plt.legend()
#exit()
plt.show()

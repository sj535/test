import numpy as np
import matplotlib.pyplot as plt

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

#r'2008'	r'2009'	r'2010'	r'2011'	r'FY12'	r'FY13'	r'FY14'	r'FY15'	r'FY16'	r'9M17'



#plt.set_title('style: {!r}'.format(sty), color='C0')
#plt.plot([r'2007', r'2008', r'2009', r'2010'], [-25, 4, 9, 56],color='#2df1ff',linestyle=':',markersize=14,label='test')
#plt.plot([r'2007', r'2008', r'2009', r'2011'], [-20, 5, 14, 40],color='#2df1ff',linestyle='--',markerfacecolor='blue', markersize=12)

plt.plot([r'2007', r'2008', r'2009', r'2010'], [-25, 4, 9, 56],color='#00f2ff',linestyle='-',markersize=14,linewidth=2,label='test')
plt.plot([r'2007', r'2008', r'2009', r'2011'], [-10, 2, 24, 50],color='#00f2ff',linestyle='--',markersize=16,linewidth=2)
plt.plot([r'2007', r'2008', r'2009', r'2010'], [-10, 2, 4, 40],color='#00f2ff',markevery=100,linestyle='--',markersize=16,linewidth=2)
plt.plot([r'2007', r'2008', r'2009', r'2011'], [-20, 5, 14, 40],color='#ff6100', marker='o',linestyle='-', linewidth=2, markersize=6)
plt.title('Sales Growth')

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
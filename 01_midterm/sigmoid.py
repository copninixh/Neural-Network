import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-10,10,0.1)
y = np.arange(-10,10,0.1)
X,Y = np.meshgrid(x,y)
z =  -1.5+X+Y > 0
z = z.astype(int)

z_sigmoid = 1/(1 + np.exp(-(-1.5+X+Y)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, z)
ax.plot_surface(X, Y, z_sigmoid)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()
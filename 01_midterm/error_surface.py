import numpy as np
import matplotlib.pyplot as plt

w1=np.arange(-10,10,0.1)
w2=np.arange(-10,10,0.1)
w1,w2=np.meshgrid(w1,w2)
w1.shape

z=((-1.8+w2>0)**2+(-1.8+w1>0)**2+((-1.8+w1+w2>0)-1)**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # Use add_subplot with projection='3d'
ax.plot_wireframe(w1,w2,z,rstride=5, cstride=5)
ax.view_init(-10, 10)
plt.show()

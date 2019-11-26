import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10,10)
y=np.square(x)
plt.xlabel('x-label')
plt.ylabel('y-label')
plt.plot(x,y)
plt.show()

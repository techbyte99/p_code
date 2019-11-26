import matplotlib.pyplot as plt
import numpy as np
y=[89,90,67,78,74]
x=['2004','2005','2006','2007','2008']
x_pos=np.arange(len(x))
plt.bar(x_pos,y,color='red')
plt.xlabel("year")
plt.ylabel("marks")
plt.title("marks of students in successive five years")
plt.show()

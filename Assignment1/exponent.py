import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(0,2,100)
y = np.exp(x)
plt.ylim(0,8,1)
plt.plot(x,y)
plt.show()

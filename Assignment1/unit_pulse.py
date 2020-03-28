from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 2, 5000)
plt.plot(t, signal.square(2 * np.pi * 5 * t))
plt.ylim(-2, 2)
plt.show()

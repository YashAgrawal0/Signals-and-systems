import matplotlib.pyplot as plt
import numpy as np

f = input("Enter Frequency of sine wave :  ")

Fs = 8000
time = 8000
x = np.arange(time)
y = np.sin(2 * np.pi * f * x / Fs)
# print(x)
plt.ylim(-1.5,1.5)
plt.plot(x, y)
plt.xlabel('t')
plt.ylabel('y(t) (sine wave)')
plt.grid(True)
plt.show()

from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy
import math


fs1,data1=wavfile.read('original.wav')
fs2,data2=wavfile.read('noisy.wav')


data=scipy.ndimage.filters.gaussian_filter(data2,20,order=2, output=None, mode='reflect', cval=0.0, truncate=2.0)
data=data2-data
sigma = raw_input("Enter value of sigma :  ")
# gauss = 1/(math.sqrt(2)*math.pi*sigma*sigma)

fin_data = []

for i in data :
	i =  i*sigma
	fin_data.append(i)

wavfile.write('out.wav',fs2,data)

plt.subplot(221)
plt.title("Original Signal")
plt.plot(data1)

plt.subplot(222)
plt.title("Noisy Signal")
plt.plot(data2)

plt.subplot(223)
plt.title("Resulting Signal")
plt.plot(data)

plt.show()	

from scipy.io.wavfile import read,write
import numpy as np
import math
import matplotlib.pyplot as plt

fr1,input_data1 = read("sounds/part_0.wav")
fr2,input_data2 = read("sounds/part_19.wav")
fr3,input_data3 = read("sounds/part_22.wav")

n1 = np.arange(0,len(input_data1))
n2 = np.arange(0,len(input_data2))
n3 = np.arange(0,len(input_data3))

magnitude1 = []
phase1 = []
magnitude2 = []
phase2 = []
magnitude3 = []
phase3 = []

N = np.arange(0,0.1,0.01)

for w in N:
	a1 = 0
	a2 = 0
	a3 = 0
	b1 = 0
	b2 = 0
	b3 = 0

	print(w)

	for i in range(0,len(input_data1)):
		a1 += input_data1[i]*math.cos(n1[i]*w)
		b1 += input_data1[i]*math.sin(w*n1[i])
		a2 += input_data2[i]*math.cos(n2[i]*w)
		b2 += input_data2[i]*math.sin(w*n2[i])
		a3 += input_data3[i]*math.cos(n3[i]*w)
		b3 += input_data3[i]*math.sin(w*n3[i])

	magnitude1.append(math.sqrt(a1**2+b1**2))
	phase1.append(math.atan(b1/a1))
	magnitude2.append(math.sqrt(a2**2+b2**2))
	phase2.append(math.atan(b2/a2))
	magnitude3.append(math.sqrt(a3**2+b3**2))
	phase3.append(math.atan(b3/a3))

plt.figure()
plt.subplot(311)
plt.title("Sound Files Waveforms")
plt.ylabel("part_0.wav  -->")
plt.xlabel("n  -->")
plt.plot(input_data1,color="blue")
plt.subplot(312)
plt.ylabel("part_19.wav  -->")
plt.xlabel("n  -->")
plt.plot(input_data2,color="green")
plt.subplot(313)
plt.ylabel("part_22.wav  -->")
plt.xlabel("n  -->")
plt.plot(input_data3,color="red")

plt.figure()
plt.subplot(321)
plt.plot(N,magnitude1,color="blue")
plt.subplot(323)
plt.plot(N,magnitude2,color="blue")
plt.subplot(325)
plt.plot(N,magnitude3,color="blue")
plt.subplot(322)
plt.plot(N,phase1,color="green")
plt.subplot(324)
plt.plot(N,phase2,color="green")
plt.subplot(326)
plt.plot(N,phase3,color="green")

plt.show()
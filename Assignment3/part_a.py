import numpy as np
import math
import matplotlib.pyplot as plt

n1 = int(raw_input("Enter n1 : "))
n2 = int(raw_input("Enter n2 : "))

length = n2-n1+1

arr = []
x_n = []
n = np.arange(n1,n2+1)
arr = raw_input("Enter value of input signal of length %d : "%length).split()

for i in arr:
	x_n.append(int(i))

magnitude = []
phase = []

N = np.arange(0,10,0.01)

for w in N:
	a = 0
	b = 0

	for i in range(0,length):
		a += x_n[i]*math.cos(n[i]*w)
		b += x_n[i]*math.sin(w*n[i])

	magnitude.append(math.sqrt(a**2+b**2))
	phase.append(math.atan(b/a))

print(phase)
plt.subplot(211)	
plt.xlabel("Omega  ---> ")
plt.ylabel("|X(e^jw)|  ---> ")
plt.title("Magnitude vs w(omega)")
plt.plot(N,magnitude)
plt.subplot(212)	
plt.xlabel("Omega  ---> ")
plt.ylabel("<) X(e^jw)  ---> ")
plt.title("Phase vs w(omega)")
plt.plot(N,phase)

plt.show()
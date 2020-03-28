from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
def impulse(x1,x2):
	a = np.zeros(3)   
	a[0:3] = 1.0      
	plt.plot([0,0],[0,1],'b')
	plt.plot([2,2],[1,0],'b')
	if x1 < 0 :
		plt.plot([x1,0],[0,0],'b')
	if x2>2:
		plt.plot([2,x2],[0,0],'b')	
	plt.plot(a)
	plt.show()

print("Let x1,x2 be the intervals\n")
x1 = input("Enter x1 :  ")
x2 = input("Enter x2 :  ")
plt.ylim(-2,2)
plt.xlim(x1,x2)
impulse(x1,x2)

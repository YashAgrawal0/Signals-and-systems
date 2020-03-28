import numpy as np

#n1 = raw_input("Input size of x[n] ")

x = raw_input("Enter values of x[n] : ").split(' ')
y = raw_input("Enter values of h[n] : ").split(' ')

arr1 = np.array(x,dtype = float)
arr2 = np.array(y,dtype = float)

print "The convolve output will be : 	"
print np.convolve(arr1,arr2)


import numpy,matplotlib
from matplotlib import pyplot as plt 
from matplotlib import style
from numpy import sin,cos,pi

def pulse(x1,x2):
	for i in range(x1,x2+1):
		plt.plot([i,i],[0,1],'g',linewidth=2)
	for i in range(x1,x2,2):
		plt.plot([i,i+1],[1,1],'g',linewidth=2)
	for i in range(x1+1,x2,2):
		plt.plot([i,i+1],[0,0],'g',linewidth=2)

plt.plot([3,3],[3,3])

style.use('ggplot')
# for i in range(5):
a = numpy.linspace(-2*pi,2*pi,100)

ysin = sin(a)
ycos = cos(a)

# plt.plot(a,ysin)
# plt.plot(a,ycos)
# for i in range(5):
# 	plt.plot([x,x],[y,y+1],'b',linewidth=5)
# 	plt.plot([x,x+1],[y+1,y+1],'b',linewidth=5)
# 	x = x+1
# 	y = y+1
# x = [1,1]
# y = [12,16,6]
x1 = int(input())
x2 =int(input())
pulse(x1,x2)

# for i in range(1,5):
# 	plt.plot([i,i],[0,1],'g',linewidth=5)
# for i in range(1,5):
# 	plt.plot([])
# for i in range(5):	
# 	plt.plot([i,1],[1,1],'g',linewidth=3)
# plt.plot([3,4],[4,5],'y',label='line1',linewidth=5)

plt.title('Graph')
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')

plt.legend()
plt.grid(True,color='k')

plt.show()
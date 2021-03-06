import numpy as np 
import matplotlib.pyplot as plt

x1 = []
x2 = []
y1 = []
y2 = []
x3 = []
y = []
y_dash = []

fig = plt.figure()
a = 1;
b = 1;

t = np.linspace(-5,5,5000,endpoint=True)

def impulse(i):
		if(i<=2 and i>=0) :
			return 1
		else :	
			return 0


for i in t:
	x1.append(impulse(i))
x2 = np.sin(t)

for i in range (len(x1)):
	x3.append(a*x1[i]+b*x2[i])

# y_dash = np.exp(x3)
for i in x3:
	y_dash.append(np.exp(-i))
for i in x1:
	y1.append(np.exp(-i))
for i in x2:
	y2.append(np.exp(-i))
y1 = np.exp(x1)
y2 = np.exp(x2)

for i in range(len(y1)):
	y.append(a*y1[i]+b*y2[i])

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.plot(t,y_dash,'b')
ax1.plot(t,y,'g')

t0 = 1

t_dash = np.linspace(-5+t0,5+t0,5000,endpoint=True)

x5 = []
x6 = []
y5 = []
y6 = []

for i in t :
	x5.append(impulse(i-t0))

for i in x5:
	y5.append(np.exp(-i))

for i in t:
	x6.append(impulse(i))

for i in x6:
	y6.append(np.exp(-i))	

# ax2.plot(t,x6,'g')
ax2.plot(t,y5,'g')
# ax2.plot(t_dash,y6,'b')
# print(len(t_dash))
# print(len(y6))
ax2.plot(t_dash,y6,'b')

plt.show()


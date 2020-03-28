import numpy as np
a = np.zeros( (1000,) )   # whatever size. initializes to zeros
a[150:180] = 1.0          # index range sets location, width of impulse
# To see a plot:

import matplotlib.pyplot as mp
mp.ylim(-2,2)
mp.plot(a)
mp.show()
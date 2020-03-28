from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy
import math


fs1,data1=wavfile.read('original.wav')

# sigma = raw_input("Enter value of sigma :  ")

# output = []

# for i in data1 :
# 	i = i*sigma
# 	output.append(i)

wavfile.write('out.wav',fs1,data1)
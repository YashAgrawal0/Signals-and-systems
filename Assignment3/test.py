from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt
from math import exp
import numpy as np

# read audio samples
input_data = read("sounds/part_22.wav")
audio = input_data[1]
fs = input_data[0]
output_arr = []
summ = 0
ind = 0
length = len(audio)
t = np.arange(length)

for i in audio[0:length]:
	summ = summ + i*exp(-ind)
	ind = ind + 1 

output = t*summ
# write("workin.wav",fs,audio)
# print(audio[20])
# plot the first 1024 samples
plt.plot(output)
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Sample Wav")
# display the plot
plt.show()

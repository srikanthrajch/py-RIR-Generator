import numpy as np
import rirgenerator as RG
import matplotlib.pyplot as plt

c = 340						# Sound velocity (m/s)
fs = 16000					# Sample frequency (samples/s)
r = [[2,1.5,2],[1,1.5,2]]	# Receiver positions [x_1 y_1 z_1 ; x_2 y_2 z_2] (m)
s = [2,3.5,2]				# Source position [x y z] (m)
L = [5,4,6]					# Room dimensions [x y z] (m)
beta = 0.4					# Reverberation time (s)
n = 4096					# Number of samples
mtype = 'omnidirectional'	# Type of microphone
order = -1					# -1 equals maximum reflection order!
dim = 3						# Room dimension
orientation = 0				# Microphone orientation (rad)
hp_filter = 1				# Enable high-pass filter

h = RG.rir_generator(c, fs, r, s, L, beta=beta, nsample=n, mtype=mtype, order=order, dim=dim, orientation=orientation, hp_filter=hp_filter)

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(h[0,:])
axarr[1].plot(h[1,:])
plt.show()

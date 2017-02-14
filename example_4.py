import numpy as np
import rirgenerator as RG
import matplotlib.pyplot as plt

c = 340						# Sound velocity (m/s)
fs = 16000					# Sample frequency (samples/s)
r = [2,1.5,2]				# Receiver position [x y z] (m)
s = [2,3.5,2]				# Source position [x y z] (m)
L = [5,4,6]					# Room dimensions [x y z] (m)
n = 4096					# Number of samples
beta = 0.4					# Reverberation time (s)
mtype = 'hypercardioid'		# Type of microphone
order = -1					# -1 equals maximum reflection order!
dim = 3						# Room dimension
orientation = [np.pi/2,0]		# Microphone orientation (rad)
hp_filter = 0				# Disable high-pass filter

h = RG.rir_generator(c, fs, r, s, L, beta=beta, nsample=n, mtype=mtype, order=order, dim=dim, orientation=orientation, hp_filter=hp_filter)

plt.plot(h[0,:])
plt.show()

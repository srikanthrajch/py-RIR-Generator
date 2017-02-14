import numpy as np
import rirgenerator as RG
import matplotlib.pyplot as plt

c = 340					# Sound velocity (m/s)
fs = 16000				# Sample frequency (samples/s)
r = [2,1.5,2]			# Receiver position [x y z] (m)
s = [2,3.5,2]			# Source position [x y z] (m)
L = [5,4,6]				# Room dimensions [x y z] (m)
beta = 0.4				# Reverberation time (s)
n = 4096				# Number of samples

h = RG.rir_generator(c, fs, r, s, L, beta=beta, nsample=n)

plt.plot(h[0,:])
plt.show()

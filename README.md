# py-RIR-Generator
This is a python compilation of the RIR-Generator code from https://github.com/ehabets/RIR-Generator


Cython is used to compile the code.

Code is taken from the Version: 2.1.20141124 of RIR-Generator.

This package contains:
	- C implementation of the RIR code and the corresponding .h file
	- A .pyx fil,e which is a wrapper code written in Cython 
	- A setup.py file to compile the new module


Python dependencies: cython

Compilation:
	python setup.py build_ext --inplace

-- The system object file rirgenerator.so generated after successful compilation is equivalent to the .mexa64 generated for MATLAB version. 

Use case:
import rirgenerator as RG

h = RG.rir_generator(c, fs, r, s, L, beta=beta, nsample=n, mtype=mtype, order=order, dim=dim, orientation=orientation, hp_filter=hp_filter)

Input parameters:
	c           : sound velocity in m/s.
	fs          : sampling frequency in Hz.
	r           : M x 3 array specifying the (x,y,z) coordinates of the receiver(s) in m.
	s           : 1 x 3 vector specifying the (x,y,z) coordinates of the source in m.
	L           : 1 x 3 vector specifying the room dimensions (x,y,z) in m.
------ Parameters below needs to be specified as: key=value 
---------ex: beta=0.4,nsample=4096,mtype='omnidirectional',order=-1,dim=3,orientation=0,hp_filter=1
	beta        : 1 x 6 vector specifying the reflection coefficients
					[beta_x1 beta_x2 beta_y1 beta_y2 beta_z1 beta_z2] or
					beta = reverberation time (T_60) in seconds.
	nsample     : number of samples to calculate, default is T_60*fs.
	mtype       : [omnidirectional, subcardioid, cardioid, hypercardioid,bidirectional], default is omnidirectional.
	order       : reflection order, default is -1, i.e. maximum order.
	dim         : room dimension (2 or 3), default is 3.
	orientation : direction in which the microphones are pointed, specified using 
					azimuth and elevation angles (in radians), default is [0 0].
	hp_filter   : use '0' to disable high-pass filter, the high-pass filter is enabled by default.

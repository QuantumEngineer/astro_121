import numpy as np
import pylab as py 
import radiolab as rd

N = 2**14
vsample = 1.0e6
delt = 1.0/vsample
time_array = np.arange(0,N)*delt
filename= "vsig_1050000.0.npz" 

data = np.load(filename)["arr_0"]

fft_data = abs(np.fft.fft(data))**2 
print np.fft.fftfreq(N,delt)
py.subplot(2,1,1)
py.plot(time_array[0:2**12],data[0:2**12])

py.subplot(2,1,2) 
py.plot(np.fft.fftfreq(N,delt),fft_data)

py.show()
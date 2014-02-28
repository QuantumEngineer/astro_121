import numpy as np
import pylab as py 


N = 2**14
vsample = 20e6
delt = 1.0/vsample
time_array = np.arange(0,N)*delt
filename= "vsig_1900000.0.npz" 
data = np.load(filename)["data"]
fft_data = abs(np.fft.fft(data))**2 


py.subplot(2,1,1)
py.plot(time_array[0:2**10]*1e6,data[0:2**10])
py.xlim([10,40])
py.xlabel('time ($\mu s$)')
py.ylabel('Voltage (V)')

py.subplot(2,1,2) 

py.plot(np.fft.fftfreq(N,delt)/1e6,fft_data/1e6)

py.ylabel('Intensity (dBm)')
py.xlabel('Frequency (MHz)')


py.figure()

filename= "vsig_2100000.0.npz" 
data = np.load(filename)["data"]
fft_data = (np.fft.fft(data)) 


py.subplot(2,1,1)
py.plot(time_array[0:2**10]*1e6,data[0:2**10])
py.xlim([10,40])
py.xlabel('time ($\mu s$)')
py.ylabel('Voltage (V)')

py.subplot(2,1,2) 
py.plot(np.fft.fftfreq(N,delt)/1e6,fft_data/1e6)
py.xlim([-3,3])
py.ylabel('Intensity (dBm)')
py.xlabel('Frequency (MHz)')

py.show()

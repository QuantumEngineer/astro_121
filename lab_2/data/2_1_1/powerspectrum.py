import numpy as np
import pylab as py 


N = 2**14
vsample = 10e6
delt = 1.0/vsample
time_array = np.arange(0,N)*delt
filename= "vsig_950000.0.npz" 
data = np.load(filename)["arr_0"]
fft_data = abs(np.fft.fft(data))**2 


py.subplot(2,1,1)
py.plot(time_array[0:2**9]*1e6,data[0:2**9])
py.xlim([10,40])
py.xlabel('time ($\mu s$)')
py.ylabel('Voltage (V)')
py.title('Lower Side Bound')

py.subplot(2,1,2) 
py.plot(np.fft.fftfreq(N,delt)/1e6,fft_data/1e6)
py.xlim([-3,3])
py.ylabel('Intensity (dBm)')
py.xlabel('Frequency (MHz)')


py.figure()

filename= "vsig_1050000.0.npz" 
data = np.load(filename)["arr_0"]
fft_data = abs(np.fft.fft(data))**2 


py.subplot(2,1,1)
py.plot(time_array[0:2**9]*1e6,data[0:2**9])
py.xlim([10,40])
py.xlabel('time ($\mu s$)')
py.ylabel('Voltage (V)')
py.title('Upper Side Bound')

py.subplot(2,1,2) 
py.plot(np.fft.fftfreq(N,delt)/1e6,fft_data/1e6)
py.xlim([-3,3])
py.ylabel('Intensity (dBm)')
py.xlabel('Frequency (MHz)')

py.show()

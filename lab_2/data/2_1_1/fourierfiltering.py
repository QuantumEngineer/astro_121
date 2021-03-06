import numpy as np
import pylab as py 


N = 2**14
vsample = 20e6
delt = 1.0/vsample
time_array = np.arange(0,N)*delt
filename= "vsig_1900000.0.npz" 
data = np.load(filename)["data"]
fft_data = abs(np.fft.fft(data))**2
filter = {'low':-.5e6, 'high':.5e6}
filtered = []

for i in range(len(fft_data)): 
    if fft_data[i] < filter['low']: 
        filtered.append(fft_data[i]*0)
    elif fft_data[i] >= filter['low'] & fft_data[i] >= filter['high']: 
        filtered.append(fft_data[i]*1)
    elif fft_data[i] > filter['high']:
        filtered.append(fft_data[i]*0)
    
py.plot(filtered)
py.show()

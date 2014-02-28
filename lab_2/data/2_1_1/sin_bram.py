import numpy as np
import pylab as py 

data = np.fromfile('sin_bram','>i')
py.plot(data) 

py.figure()
fft_data = abs(np.fft.fft(data))

py.plot(fft_data) 
py.show()


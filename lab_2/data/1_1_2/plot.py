import numpy as np 
import pylab as py  


filename = "f_10000Hz.npz"
data = np.load(filename)['arr_0']    
N = 256
sampling = 10e4
py.subplot(2,1,1)
t = np.arange(0,N,1)*(sampling)**(-1)
py.plot(t,data)
py.ylim([-1,1.5])

py.title('$v_{sig} = v_{sample}$', fontsize=15, horizontalalignment='right', verticalalignment='baseline')

py.xlabel('time ($\mu$s)')
py.ylabel("Voltage (V)")

filename = "fast_signal.npz"
data = np.load(filename)['arr_0']    
N = 256
sampling = 7e4
py.subplot(2,1,2)
t = np.arange(0,N,1)*(sampling)**(-1)
py.plot(t,data)


py.title('$v_{signal}/v_{sample} = 1429$', fontsize=15, horizontalalignment='right', verticalalignment='baseline')
py.xlabel('time ($\mu$s)')
py.ylabel("Voltage (V)")
py.show()

import DFEC 
import pylab as py 
import numpy as np 
sampling = 1e7
N = 256

for i in np.arange(0.1,1.0,.1):
    freq_signal = sampling*i             
    DFEC.set_srs(1,freq=freq_signal,dbm=0,pha=180)
    DFEC.set_srs(2,freq=freq_signal,dbm=0,pha=180)
    data = DFEC.sampler(N,sampling)
    filename = "%svsample_10MHz.npz" % i
    np.savez(filename,data,sampling,N)
    raw_input("Press enter to continue sampling...")
    
    






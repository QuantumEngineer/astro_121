import DFEC
import numpy as np 
import pylab as py 

vlo = 1e6 #1 KHz
delv = .05*vlo
vsighigh = vlo + delv
vsiglow = vlo - delv
vsample = 10e6 
N = 2**14

for vsig in [vsiglow, vsighigh]: 
    DFEC.set_srs(2, freq=vsig,dbm=1, pha=0)
    DFEC.set_srs(1, freq=vlo, dbm=7, pha=0)
    print 'RF srs_2 = ' + str(vsig/1000000.0) + ' MHz  and V = .75'  
    print 'LO srs_1 = ' + str(vlo/1000000.0) + ' MHz and V = .25' 
    raw_input("Start data collection?")
    data = DFEC.sampler(N,vsample)
    filename = "vsig_%.1f.npz" % vsig
    np.savez(filename,data)
    print "Saved %s" % filename


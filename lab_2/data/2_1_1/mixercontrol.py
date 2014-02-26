import DFEC
import numpy as np 
import pylab as py 

vlo = 1e6 #10 KHz
delv = .05*vlo
vsighigh = vlo + delv
vsiglow = vlo - delv
vsample = {str(vsiglow):(2.0*vsiglow),str(vsighigh):(2.0*vsighigh)} 
N = 2**14

for vsig in [vsiglow, vsighigh]: 
   # DFEC.set_srs(1, freq=vsig, dbm=0, pha=180)
   # DFEC.set_srs(2, freq=vlo, dbm=0, pha=180)
    print 'RF srs_2 = ' + str(vsig/1000000.0) + ' MHz  and V = .75'  
    print 'LO srs_1 = ' + str(vlo/1000000.0) + ' MHz and V = .25' 
    raw_input("Start data collection?")
    data = DFEC.sampler(N,vsample[str(vsig)])
    filename = "vsig_%.1f.npz" % vsig
    np.savez(filename,data)
    print "Saved %s" % filename


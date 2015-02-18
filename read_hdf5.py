import h5py
import numpy as np

f = h5py.File('mom_Ions.h5', 'r')

tpar = f['/mom_Ions/T_par']

test = tpar['0000000000']
print('time = ', test.attrs['time'])
print(test[0,0,0])

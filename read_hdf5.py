import h5py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read HDF5 file
f = h5py.File('mom_Ions.h5', 'r')
mom = f['/mom_Ions']

# Read variables
tpar_h5 = mom['T_par']
tperp_h5 = mom['T_perp']
density_h5 = mom['dens']
qpar_h5 = mom['q_par']
qperp_h5 = mom['q_perp']
upar_h5 = mom['u_par']

time = np.array(mom['time'])

# Variable index is in the form of an array of strings indexing time steps
idx = np.array(mom['T_par'])

density = np.array(density_h5[idx[0]])
shape = density.shape

# Convert to complex number
field = np.empty(shape, dtype=complex)
for i in range(shape[0]):
    for j in range(shape[1]):
        for k in range(shape[2]):
            field[i,j,k] = float(density[i,j,k][0]) + 1j*float(density[i,j,k][1])

plt.contourf(np.real(field[:,:,0]), cmap='coolwarm')
plt.show()



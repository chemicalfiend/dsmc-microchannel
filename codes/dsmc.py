# Direct Simulation Monte Carlo Simulation for flow through a channel.

import matplotlib.pyplot as plt
import numpy as np
from scipy import special



def dsmc():
    density = 1e-3
    N = 50000
    lam = 1/(np.sqrt(2) * np.pi * density)
    L = 225 
    R = 20
    Kn = lam / L
    
    numcells = 50

    dt = 0.001
    dr = R/numcells
    dtheta = 2 * np.pi / numcells

    T = 1.0  # Temperature in kT units

    volume = np.pi * (dr)**2 * L / numcells
    

    r = dr * np.random.random(N)
    theta = dtheta * np.random.random(N)
    z = L * np.random.random(N)

    vr = np.random.normal(0, T, N)
    vtheta = np.random.normal(0, T, N)
    vz = np.random.normal(2, T, N)

    timesteps = 5000

    vr0 = np.zeros(timesteps)  # Recording values of vr to generate plot

    for i in range(timesteps):
        r += dt*vr
        theta += dt*vtheta
        z += dt*vz
        

        # If particle hits wall of channel

        hit_wall = r > R
        dt_ac = (r[hit_wall]-R) / vz[hit_wall]
        vr[hit_wall] = -vr[hit_wall]
        r[hit_wall] = R + dt_ac * vz[hit_wall]
        
        hit_wall2 = r < -R

        dt_ac = (R - r[hit_wall]) / vz[hit_wall]
        vr[hit_wall] = -vr[hit_wall]
        r[hit_wall] = -R + dt_ac * vz[hit_wall]
        

    
    # Plot vz profile

    bin_c = dr * np.linspace(0.5-numcells,numcells-0.5,numcells)
    vz_profile = np.zeros((numcells, 1))

    for j in range(numcells):
        in_cell = (j*dr < r) & (r < (j+1)*dr)
        if len(vz[in_cell]) > 0:
            vz_profile[j] = np.mean(vz[in_cell])
        else:
            vz_profile[j] = 0
    
    plt.xlabel("r")
    plt.ylabel("vz")
    plt.plot(bin_c, vz_profile)
    plt.savefig('dsmc.png',dpi=240)
    plt.show()


if __name__ == "__main__":
    dsmc()

        



        


    







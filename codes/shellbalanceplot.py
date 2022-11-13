# Plot of analytical solution from shell momentum balance

import matplotlib.pyplot as plt
import numpy as np

R = 20
M = 2
r = np.linspace(-R, R, 100)
vz = M * (1 - (r/R)**2)
plt.xlabel("r")
plt.ylabel("vz")
plt.plot(r, vz)
plt.savefig("shellbalance.png")
plt.show()



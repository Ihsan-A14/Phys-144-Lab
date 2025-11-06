import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

csv = pd.read_csv('pendulum data.csv')

# Grabbing values from the Table
t = csv['t']
KE = csv['ke']
PE = csv['pe']
TE = csv['te']
lnE = csv['lne']

# 1. Energy plot
plt.figure()
plt.plot(t, KE, linestyle = '--', label='Kinetic Energy')
plt.plot(t, PE, linestyle = '', marker = 'o', label='Potential Energy') 
plt.plot(t, TE, label='Total Energy')

# Aesthetics of the Graph
plt.xlabel("time (s)", fontsize=16)
plt.ylabel("Energies (J) ", fontsize=16)
plt.xticks(fontsize=14, color= (23/2551, 84/255, 128/255))
plt.yticks(fontsize=16, color="purple")
plt.legend(loc='upper right', prop={'size': 7})
plt.title('Graph of Kinetic, Potential, and Total Energies of Pendulum vs Time')

# 2. Linearise the data
fitpar, uncert = np.polyfit(t, lnE, 1, cov = True)

slope = fitpar[0]
intercept = fitpar[1]

slope_unc = np.sqrt(uncert[0][0])
intercept_unc = np.sqrt(uncert[1][1])

print(slope, slope_unc)

tau = -1 / slope
tau_uncert = abs(tau) * (slope_unc / abs(slope))

print('characteristic timescale for energy loss, 𝜏 =', tau ,'±', tau_uncert)

print ('initial Energy =', intercept,'±', intercept_unc)
plt.plot(t, lnE, 'bo', label='Data')
plt.plot(t, slope*t + intercept, 'r-', label=f'Fit: slope = {slope:.3f} ± {slope_unc:.3f}')
plt.xlabel('Time (s)')
plt.ylabel('ln(E)')
plt.xticks(fontsize=14, color= (23/2551, 84/255, 128/255))
plt.yticks(fontsize=16, color="purple")
plt.legend(loc='upper right', prop={'size': 7})
plt.title('Liearized Graph of ln(E) vs Time')
plt.show()

# 3. FInding time when energy becomes 1/100 initial energy
import math
t_1_100 = tau * math.log(100)
t_1_100_uncert = tau_uncert * math.log(100)  # Propagate uncertainty

print(f"Time to 1/100 energy: {t_1_100:.1f} ± {t_1_100_uncert:.1f} s")

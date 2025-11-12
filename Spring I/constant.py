import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

# 1. Hooke's Law estimation of spring constant
csv = pd.read_csv('hooke.csv')

force = csv['Force, F (N)']
exten = csv['Extension, Δx (m)']

plt.plot(exten, force, linestyle = ' ', marker = 'o', label = 'Experiment Data')

# Linearizing the graph
fitpar, uncert = np.polyfit(exten, force, 1, cov = True)

a1 = fitpar[0]
a2 = fitpar[1]

er1 = np.sqrt(uncert[0][0])
er2 = np.sqrt(uncert[1][1])

print('Slope of the graph :',a1, '±', er1)
print('Intercept of the graph :', a2, '±', er2)

k = a1
k_uncert = er1

print('Spring constant :', k, '±', k_uncert)

f_update = a1 * exten + a2

plt.plot(exten, f_update, linestyle = '-', label = 'Linear Fit Data')
plt.xlabel('Extension, Δx (m)')
plt.ylabel('Applied Force, F (N)')
plt.title('Hooke\'s Law: Applied Force vs. Extension')
plt.legend(loc='best', prop={'size': 10})


# 2. Finding k using the period of oscillation
csv = pd.read_csv('oscillation.csv')

xaxis = csv['Mass (kg)']
yaxis = csv['T²/(4π²) (s²)']

plt.plot(xaxis, yaxis, linestyle = ' ', marker = 'o', label = 'Experiment Data')

# Linearizing the graph
fitpar, uncert = np.polyfit(xaxis, yaxis, 1, cov = True)

a1 = fitpar[0]
a2 = fitpar[1]

er1 = np.sqrt(uncert[0][0])
er2 = np.sqrt(uncert[1][1])

print('Slope of the graph :',a1, '±', er1)
print('Intercept of the graph :', a2, '±', er2)

k = 1/a1
k_uncert = (er1 / (a1**2))

print('Spring constant :', k, '±', k_uncert)

# Mass of rubber band
m_s = 3 * k * a2
m_s_uncert = 3 * k * np.sqrt((er2)**2 + (a2 * k_uncert / k)**2)

print('Mass of rubber band from oscillations:', m_s, '±', m_s_uncert, 'kg')

y_update = a1 * xaxis + a2

plt.plot(xaxis, y_update, linestyle = '-', label = 'Linear Fit Data')
plt.ylabel('T²/(4π²) (s²)')
plt.xlabel('Mass (kg)')
plt.title('Simple Harmonic Motion')
plt.legend(loc='best', prop={'size': 10})
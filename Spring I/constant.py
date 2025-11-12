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
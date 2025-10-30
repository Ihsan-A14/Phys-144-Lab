import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

csv = pd.read_csv('helium spectrum 2.csv')

# Grabbing the values from the data table
wl = np.array(csv['Wavelength '])
sin = np.array(csv['Sin'])

# plotting the initial graph in scatter format
plt.plot(sin, wl, linestyle = ' ', marker = 'o', label = 'Initial Helium Spectrum Data')

# Creating Linearised data and finding d
fitpar, uncer = np.polyfit(sin, wl, 1, cov = True)

a1 = fitpar[0]
a0 = fitpar[1]

er1 = np.sqrt(uncer[0][0])
er0 = np.sqrt(uncer[1][1])

# Printing slope and intercept of the graph along with their uncertainities
print("Slope of graph, d = ", a1, "±", er1)
print("Intercept of graph = ", a0, "±", er0)

# Data for best-fit graph
sin_fit = np.linspace(min(sin), max(sin), 100)
wl_fit = a1 * sin_fit + a0

# Plotting the linearised graph
plt.plot(sin_fit, wl_fit, linestyle = '-', label = 'Linearized helium Spectrum Data')


# Aesthetics of the Graph
plt.xlabel("sin θ", fontsize=16)
plt.ylabel("Wavelength λ (nm) ", fontsize=16)
plt.xticks(fontsize=14, color= (23/2551, 84/255, 128/255))
plt.yticks(fontsize=16, color="purple")
plt.legend(loc='best', prop={'size': 10})
plt.title('Graph of Wavelength - sin θ of Helium Emission Spectrum')
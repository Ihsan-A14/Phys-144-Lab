import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

csv = pd.read_csv('helium spectrum.csv')

wl = np.array(csv['Wavelength '])
sin = np.array(csv['Sin'])


plt.plot(sin, wl, linestyle = ' ', marker = 'o', label = 'Initial Data')


plt.xlabel("sin theta (rad)", fontsize=16)
plt.ylabel("Wavelength (mm) ", fontsize=16)
plt.xticks(fontsize=14, color= (23/2551, 84/255, 128/255))
plt.yticks(fontsize=16, color="purple")
plt.legend(loc='best', prop={'size': 10})
plt.title('Graph of Wavelength - sin theta of Helium Emission Spectrum')
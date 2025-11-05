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

# 1. Energy plot
plt.figure()
plt.plot(t, KE, linestyle = '--', label='Kinetic Energy')
plt.plot(t, PE, linestyle = '', marker = 'o', label='Potential Energy') 
plt.plot(t, TE, label='Total Energy')


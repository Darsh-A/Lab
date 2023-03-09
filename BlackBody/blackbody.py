import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# importing data
HighVol = np.loadtxt('High_Voltage.txt',delimiter=',')
LowVol = np.loadtxt('Low_Voltage.txt',delimiter=',')

def f(x,a,b):
    return a*np.log(x)+b

plt.plot(HighVol[:,0],HighVol[:,1],'bo')

popt, pcov = curve_fit(f,HighVol[:,0],HighVol[:,1])

xFit = np.arange(1.0,12.5,0.1)

plt.plot(xFit,f(xFit,*popt),'r-')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('High Voltage')
plt.show()


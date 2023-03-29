import matplotlib.pyplot as plt
import numpy as np

# V = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# I = [0.19, 0.26, 0.33, 0.39, 0.44, 0.49, 0.54, 0.58, 0.62, 0.66, 0.69, 0.73]

P = [0.52, 0.99, 1.56, 2.2, 2.94, 3.78, 4.64, 5.58, 6.6, 7.59, 8.76]
T = [981, 1149, 1292, 1426, 1530, 1621, 1720, 1807, 1885, 1980, 2040]
logP = []
logT = []

for i in P:
    logP.append(np.log10(i))

for j in T:
    logT.append(np.log10(j))

plt.plot(logT, logP, "r.")
plt.plot(logT, logP, "r")
plt.xlabel('log(T)')
plt.ylabel('log(P)')
plt.show()
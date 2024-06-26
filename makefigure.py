import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,21)
y = 0.03 * np.power(x,2)

plt.plot(x,y, linestyle='-', marker='', color='gold')
plt.plot([-3,3],[5,5], marker='o', linestyle='', color='gold')

plt.xlim([-12,12])
plt.ylim([-2,10])
plt.savefig('LEAPS.png')

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,21)
y = 3-0.03 * np.power(x,2)

plt.plot(x,y, linestyle='-', marker='', color='red')
plt.plot([-3,3],[5,5], marker='o', linestyle='', color='red')

plt.xlim([-12,12])
plt.ylim([-2,10])
plt.savefig('weather_red.png')

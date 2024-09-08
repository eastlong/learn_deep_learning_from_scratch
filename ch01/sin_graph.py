import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

x = np.arange(0, 6, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()


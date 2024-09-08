import numpy as np
import matplotlib.pylab as plt

def sigmod(x):
    return 1 / (1 + np.exp(-x))

X = np.arange(-5.0, 5.0, 0.1)
Y = sigmod(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1) # 设置y轴的范围
plt.xlim(-6.0, 6.0)
plt.show()
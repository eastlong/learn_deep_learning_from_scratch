import matplotlib.pyplot as plt
import matplotlib
from matplotlib.image import imread
matplotlib.use('TkAgg')

img = imread('../dataset/lena.png')
plt.imshow(img)

plt.show()
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt

np.random.seed(0)
f1 = plt.figure(figsize=(10, 2))
plt.title("figure size : (10, 2)")
plt.plot(np.random.randn(100))
plt.show()

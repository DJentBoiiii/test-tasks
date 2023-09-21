import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def autogen(h,v):
    return np.random.choice([0,1], size=(h,v))

arr = autogen(5,6)
print(arr)
print(np.sum(arr))


def visualize(arr):
    plt.clf()
    plt.imshow(arr, cmap='binary', interpolation='none')


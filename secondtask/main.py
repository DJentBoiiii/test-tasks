import numpy as np
import helper as hp
import matplotlib.pyplot as plt

def game_of_life(arr):
    new_state = np.zeros((arr.shape[0], arr.shape[1]))
    parr = np.pad(arr, 1, constant_values = 0)
    for row, col in np.ndindex(arr.shape):
        if(row < arr.size-1):
            alive = np.sum(parr[row:row+3, col:col+3]) - parr[row+1, col+1]

            if arr[row, col] == 1:

                if alive < 2 or alive > 3:
                    new_state[row, col] = 0
                else:
                    new_state[row, col] = 1
            else:
                if alive == 3:
                    new_state[row, col] = 1
    return new_state


def start_always():
    h=int(input("Enter number of rows: "))
    v=int(input("Enter amount of cols: "))
    arr = hp.autogen(h, v)
    im = ax.imshow(arr, cmap='binary')

    print(arr)
    plt.show()
    while True:
        arr = game_of_life(arr)
        print(arr)
        im.set_array(arr)
        plt.pause(0.0004)


    

plt.ion()
fig, ax = plt.subplots()
start_always()

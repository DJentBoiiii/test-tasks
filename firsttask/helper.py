import numpy as np

def create():
    rows = int(input("Enter row amount: "))
    cols = int(input("Enter column amount: "))
    arr = np.empty((rows, cols))

    for i in range(rows):
        row_data = input(f"Enter values for {i + 1}row with space: ")
        row_values = row_data.split()  
        for j in range(cols):
            arr[i, j] = float(row_values[j]) 
    
    return arr
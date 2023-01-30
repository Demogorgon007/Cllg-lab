import numpy as np 
 
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
length = len(matrix)

diagonals = []
for i in range(length):
    for j in range(length):
        if i ==j:
            diagonals.append(matrix[i][j])
        else:
            continue
print(diagonals)

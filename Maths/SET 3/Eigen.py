import numpy as np
from numpy.linalg import eig

def eigen(matrix):

    evalue,evector = eig(matrix)
    value = np.array(evalue)
    vector = np.array(evector)
    print(f"\nEigen Value Of The Matrix :\n\n {value}\n\n\nEigen Vector Of The Matrix :\n\n{vector}\n\n")

rows = int(input("Enter no of rows of matrix:"))
cols = int(input("Enter no of columns of matrix:"))
print("Enter matrix elements:")
matrix = []
for i in range(rows):
    a = []
    for j in range(cols):
        a.append(int(input()))
    matrix.append(a)

mat = np.array(matrix)
mat = mat.reshape(rows, cols)
print("matrix :")
print(mat)

eigen(matrix)

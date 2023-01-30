import numpy as np

r = int(input("Enter no of rows of matrix:"))
c = int(input("Enter no of columns of matrix:"))
print("Enter matrix elements:")
matrix = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

mat = np.array(matrix)
mat = mat.reshape(r, c)
print("matrix :")
print(mat)
rank = np.linalg.matrix_rank(mat)
print("Rank of the given Matrix is : ",rank)

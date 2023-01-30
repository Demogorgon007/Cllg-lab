import numpy as np

#sparsity checking
def spar(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    spr_count = 0
    count = rows*cols
    sparsity = 0

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                spr_count = spr_count+1

    sparsity = spr_count / count
    print(sparsity)

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
spar(mat)


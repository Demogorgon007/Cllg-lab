from numpy import diag
import numpy as np
from numpy import dot
from numpy.linalg import inv
from numpy.linalg import eig

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

print("\nMatrix = :")
for row in mat:
    print(row)


Evalues, Evectors = eig(matrix)



invEig = inv(Evectors)


Diagfrmvect = diag(Evalues)


rematrix = Evectors.dot(Diagfrmvect).dot(invEig)

print("\nRe-Constructed Matrix = :")
for row in rematrix:
    print(row)
import numpy as np

r = int(input("Enter the rows of matrices :"))
c = int(input("Enter the columns of matrices:"))
matrix = []
print("Enter the first matrix element in row ways : ")

for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

met = np.array(matrix)
met = met.reshape(r, c)
print("matrix :")
print(met)


matrix1 = []
print("Enter the 2nd matrix element in row ways : ")

for i in range(r):
    me = []
    for j in range(c):
        me.append(int(input()))
    matrix1.append(me)

met1 = np.array(matrix1)
met1 = met1.reshape(r, c)
print("matrix :")
print(met1)
print("Hadamard Product of 2 matrix :")
product = met1*met
print(product)

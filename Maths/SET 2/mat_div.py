import numpy as np

r = int(input("Enter the rows of matrix 1 :"))
c = int(input("Enter the columns of matrix 2:"))
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

m = int(input("Enter the rows of matrix 1 :"))
n = int(input("Enter the columns of matrix 2 :"))
matrix1 = []
print("Enter the 2nd matrix element in row ways : ")

for i in range(m):
    me = []
    for j in range(n):
        me.append(int(input()))
    matrix1.append(me)

met1 = np.array(matrix1)
met1 = met1.reshape(m, n)
print("matrix :")
print(met1)
print("Divide of 2 matrix :")
sum = np.divide(met, met1)
print(sum)
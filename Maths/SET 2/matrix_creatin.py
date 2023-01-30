import numpy as np

r = int(input("Enter the number of rows :"))
c = int(input("Enter the number of columns :"))
matrix = []
print("Enter the element in row ways : ")

for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

met = np.array(matrix)
met = met.reshape(r, c)
print("matrix :")
print(met)




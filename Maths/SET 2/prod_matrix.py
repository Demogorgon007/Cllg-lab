import numpy as np 

rows = int(input("Enter the no. of rows in 1st matrix :"))
columns = int(input("Enter the number of columns in 1st matrix :"))

column_2 = int(input("Enter the no.of columns of 2nd matrix :"))

print(f"Enter the 1st {rows} x {columns} matrix")
matrix_1 = [[int(input()) for j in range(columns)] for i in range(rows)] 

print(f"Enter the element of 2nd {columns} x {column_2} matrix")
matrix_2 = [[int(input()) for j in range(column_2)] for i in range(columns)]

print("1st matrix \n", matrix_1)
print("2nd matrix \n", matrix_2)

result = []

for i in range(rows):
    for j in range(column_2):
        sum = 0
        for k in range(columns):
            sum += matrix_1[i][k] * matrix_2[k][j]
        result.append(sum)
result = np.array(result)
result = result.reshape(rows,column_2)

print("Resultant matrix after multiplication is:\n",result)

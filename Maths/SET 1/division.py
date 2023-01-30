import numpy as np

print( "Enter the vector1:")
list1 = [int(list1) for list1 in input().split()]

print("Enter the vector2:")
list2 = [int(list2) for list2 in input().split()]

vector1 = np.array(list1)
vector2 = np.array(list2)

vector = vector1//vector2
print(vector)
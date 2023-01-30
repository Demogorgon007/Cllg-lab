import numpy as np
list1 = []
list2 = []
dimension =3
for i in range(dimension):
    #print(i)
    mul = int(input())
    list1.append(mul)
for j in range(dimension):
    mul = int(input())
    list2.append(mul)
vector1 = np.array(list1)
vector2 = np.array(list2)

vector = vector1*vector2
print(vector)
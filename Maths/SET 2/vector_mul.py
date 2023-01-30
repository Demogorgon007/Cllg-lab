import numpy as np
import math

print("enter the number1 :")
v1 = [int(v1) for v1 in input().split()]
v = np.array(v1)
print("Enter the number2 :")
v2 = [int(v2) for v2 in input().split()]
c = np.array(v2)

result = np.multiply(v,c)

print(result)
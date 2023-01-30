import numpy as nm

vector = []
vector2 = []
var = input("Enter the dimension : ")
di = int(var)
print("Enter the vector element :")

for i in range(0, di):
    ele = int(input())
    vector.append(ele)

sca = int(input("Enter the scalar value :"))
li1 = nm.array(vector)

mul = li1 * sca

print(mul)
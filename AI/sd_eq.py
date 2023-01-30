import pandas as py
import math
li = py.read_csv('Affairs.csv')

mp = li["age"]

sum = 0

l = len(mp)

for i in range(0,l):
    sum = sum+mp[i]

mean = sum/l

s = 0
for i in range(0,l):
    s = s + ((mp[i]-mean)**2)

r = math.sqrt(s)
sd = r/l
print(sd)




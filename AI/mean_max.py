import pandas as pd
import numpy as num

data = pd.read_csv("Affairs.csv")
age = data["age"]
min = num.min(age)
max = num.max(age)
mean = num.mean(age)
print(min)
print(max)
print(mean)

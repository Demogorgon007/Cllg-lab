import pandas as pd
import numpy as num

data = pd.read_csv("Affairs.csv")
age = data["age"]
sd = num.std(age)
print(sd)
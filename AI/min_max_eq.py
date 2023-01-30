import pandas as pd
import numpy as num

data = pd.read_csv("Affairs.csv")
age = data["age"]

def min_max(data):

    l = len(data)
    min = 0
    max = 0
    sum = 0
    mean = 0
    for i in range(0, l):
        if(i==0):
            min=data[i]
            max = data[i]
        if(data[i]>max):
            max = data[i]

        if(data[i]<min):
            min = data[i]

        sum = sum + data[i]
        mean = sum/l

    print("Minimum of age :", min)

    print("Minimum of age :", max)

    print("Mean of age :", mean)


min_max(age)



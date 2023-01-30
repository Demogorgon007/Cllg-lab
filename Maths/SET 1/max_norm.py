from numpy.linalg import norm
import numpy as np
from math import inf

vec = []
for v in ["i","j","k"]:
    value = int(input(f"Enter the value of {v} =>"))
    vec.append(value)
vec = np.array(vec)
n = norm(vec, inf)
print("  max norm = ",n)

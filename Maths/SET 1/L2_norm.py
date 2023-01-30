from numpy.linalg import norm
import numpy as np

vec = []
for v in ["i","j","k"]:
    value = int(input(f"Enter the value of {v} =>"))
    vec.append(value)
vec = np.array(vec)
n = norm(vec, 2)
print("  L2 norm = ",n)

import random
import math

N = 10
print(N)
a = [1, 1]
k = 3, 4
for k in range(2, N):
    x = a[k - 2] + a[k - 1]
    a.append(x)
print(a)

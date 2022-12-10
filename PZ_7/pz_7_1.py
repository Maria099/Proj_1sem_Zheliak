import random
N = random.randrange(1, 27)
print("N = ",N)
for i in range(N):
    print(chr(ord('z')-i), end=" ")
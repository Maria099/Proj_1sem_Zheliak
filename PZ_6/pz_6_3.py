#Дан список размера N. Обнулить все его локальные максимумы (то есть числа,
#большие своих соседей).

import random

N = random.randrange(3,21)
print("N = ", N)

a = [random.randrange(1,21) for i in range(N)]
print("список:\n",a)

for i in range(1,N-1):
    if a[i-1] < a[i] and a[i] > a[i+1]:
        a[i] = 9999999
for i in range(1,N-1):
    if a[i] == 9999999 :
        a[i] = 0

print("изменённый список:\n",a)
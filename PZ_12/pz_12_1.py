#Из последовательности на n целых чисел создать новую последовательность, в
#которой каждый последующий элемент равен квадрату суммы двух соседних элементов.

import random
n=0
p=-1
k=1
lst=[]
lst_new=[]
n1=30
while n1>n:
  number = random.randint(-9, 9)
  lst = lst + [number]
  n = n+1
print(lst)
n=0
while 29>n:
  lst_new = lst_new + [(lst[k]+lst[p])**2]
  p=p+1
  k=k+1
  n = n+1
print(lst_new)
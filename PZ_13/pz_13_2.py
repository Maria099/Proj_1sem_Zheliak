#Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
import random
l=0
M = int(input("Количество столбцов: "))
N = int(input("Количество строк: "))
matrix = [[random.randrange(0, 10) for y in range(M)] for x in range(N)]
c = [matrix[i]for i in range(N)]

print('Исходная матрица: ')
for i in range(N):
  print(c[i])

print("Измененная матрица: ")
for i in range(M):
  for j in range(N):
    if matrix[i][j] % 2 == 1:
        matrix[i][j] = 0

for i in range(N):
  print(f'{matrix[l]}')
  l = l+1
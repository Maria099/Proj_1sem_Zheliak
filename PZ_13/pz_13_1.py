#В матрице элементы второго столбца возвести в квадрат
import random
M = int(input("Количество столбцов: "))
N = int(input("Количество строк: "))
matrix = [[random.randrange(0, 10) for y in range(M)] for x in range(N)]
c = [matrix[i]for i in range(N)]

print('Исходная матрица: ')
for i in range(3):
  print(c[i])

print("Измененная матрица: ")
for i in range(0, len(matrix)):
  matrix[i][1]=matrix[i][1] **2

print(f'{matrix[0]}\n'
      f'{matrix[1]}\n'
      f'{matrix[2]}\n')

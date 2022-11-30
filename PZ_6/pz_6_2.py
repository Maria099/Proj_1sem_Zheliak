#Дан список A размера N и целые числа K и L (1 < K < L < N). Переставить в обратном
#порядке элементы списка, расположенные между элементами AK и AL, включая эти
#элементы.

from random import sample
n, k, l = [int(input('Введите значение "N, K, L" через Enter:\n')) for i in range(3)]
# n, k, l = [int(i) for i in input("Введите значение через запятую: \n").split(',')]
lst = sample(range(1, 100), n)
k += 1
print(*lst, sep=' | ')
lst[k:l] = lst[k:l][::-1]
print(*lst, sep=' | ')
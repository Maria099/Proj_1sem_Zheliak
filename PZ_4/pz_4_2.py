#Дано целое число N (>0). Используя операции деления нацело и взятия остатка от деления, найти количество и сумму его цифр.
a = int(input("Введите число: "))
b = 0
c = 0
while a != 0:
    d = a % 10
    b += d
    a = a // 10
    c += 1
print("Сумма цифр: ", b)
print("Количество цифр: ", c)

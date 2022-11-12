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
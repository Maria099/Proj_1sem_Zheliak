#Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1.2, 1.4, ..., 2 кг конфет
import random
price = round(random.uniform(0, 100),2)
print('Цена 1 кг конфет: ', price)
print()
for i in range(0,5):
    x = 1.2 + 0.2*i
    print('Стоимость {0:.1f} кг: {1:.2f}'.format(x, x * price))
print()

# Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
# Добавьте методы для вычисления процентных начислений и снятия денег.

class Bank:
    def __init__(self, name, surname, sum, percent):
        self.name = name
        self.surname = surname
        self.sum = sum
        self.percent = percent

    def per_accrual(self):
        return self.sum * self.percent/100

    def withdrawal(self):
        return float(input('Сумма снятия(комиссия 1%):')) * 0.99

per_1 = Bank('Maria', 'Zilyak', 130000, 7)

print('Процентные начисления: ',per_1.per_accrual(), '₽')
print('Снятие денег: ',per_1.withdrawal(), '₽')

# Создайте класс "Фрукт", который содержит информацию о наименовании и весе
# фрукта. Создайте классы "Яблоко" и "Апельсин", которые наследуются от класса
# "Фрукт" и содержат информацию о цвете
class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return f"{self.name} {self.weight}{'г.'}"

class Apple(Fruit):
    def green(self):
        print(f"{self.name} зеленое")

class Orange(Fruit):
    def orange(self):
        print(f"{self.name} оранжевый")

Apple = Apple('Яблоко', 176)
Orange = Orange('Апельсин', 198)

print(Apple.get_weight())
print(Orange.get_weight())

Apple.green()
Orange.orange()
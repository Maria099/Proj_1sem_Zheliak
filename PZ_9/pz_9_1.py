#Дан словарь с произвольным количеством элементов. Выяснить
#имеется ли в нем элемент с ключом «фрукт = яблоко» и если он отсутствует, то
#добавить его в словарь. Вывести на экран первоначальный словарь и измененный.
s = {'овощ':'картошка', 'ягода': 'черника'}
print(s)
if 'фрукт' not in s:
  s['фрукт']= 'яблоко'
print(s)

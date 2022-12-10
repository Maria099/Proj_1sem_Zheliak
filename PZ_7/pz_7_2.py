text = input('Сообщение для шифровки: ').lower()
k=int(input('Введите ограничение от 0 до 10: '))
alfavit = 'абвгдежзийклмнпрстуфхцчхщъыьэюя'
itog = ''
for i in text:
  mesto = alfavit.find(i)
  new_mesto = mesto + k
  if i in alfavit:
    itog += alfavit[new_mesto]
  else:
    itog += i
print(itog)

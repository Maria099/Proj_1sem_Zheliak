# Из предложенного текстового файла (text18-5.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно заменив символы нижнего регистра на верхний.

w = 0
m = []
for i in open('text5.txt', encoding='UTF-8'):
    print(i, end='') #выводим наш текст в консоль
    w = w + len(i)
print(end='\n')
print('Количество символов: ', w, end='\n')

for i in open('text5.txt', encoding='UTF-8'):
    m.append(i.upper()) #Заменяем символы нижнего регистра на верхний
f1 = open('text5-2.txt', 'w') #формируем новый файл
f1.writelines(m)
f1.close()
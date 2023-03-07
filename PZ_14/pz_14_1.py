#Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
#маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
#– все остальные. Посчитать количество полученных строк в каждом файле.

import re
ip_address = open('ip_address.txt', encoding='UTF-8')
read = ip_address.read()
ip_address.close()

comm_mask = re.findall(r"255.\d*.\d*.\d+\n", read)
change = re.findall(r"255.\d*.\d*\.0", read)
others = set(comm_mask).difference(set(change))

first_file = open('first_file.txt', 'w')
first_file.write(f'Строки с ненулевыми четвёртым октетом: {change}\n'
                f'Количество строк: {len(change)}')
first_file .close()

second_file = open('second_file.txt', 'w')
second_file.write(f'Остальные строки: {others}\n'
             f'Количество строк: {len(others)}')
second_file.close()

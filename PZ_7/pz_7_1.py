#Дано целое число N (1 < N < 26). Вывести N последних строчных (то есть маленьких)
#букв латинского алфавита в обратном порядке (начиная с буквы «z»).
import random
N = random.randrange(1, 27)
print("N = ",N)
for i in range(N):
    print(chr(ord('z')-i), end=" ")

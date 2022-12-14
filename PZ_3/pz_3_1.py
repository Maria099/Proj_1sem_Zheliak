#Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы
#неравенства A > 0 или B < —2».
import random
a=random.randrange(-10,10)
b=random.randrange(-10,10)
print("a=",a)
print("b=",b)
x=(a>0) and (b<-2)
print("a>0: ",(a>0))
print("b<-2: ",(b<-2))
print("a>0 и b<-2: ",x)

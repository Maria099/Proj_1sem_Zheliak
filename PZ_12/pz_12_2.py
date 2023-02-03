#Составить генератор (yield), который переведет символы строки из нижнего
#регистра в верхний.

def str_to_upper(crs: str):
    for ch in crs:
        yield ch.upper()
user_str = input()
print(''.join(str_to_upper(user_str)))
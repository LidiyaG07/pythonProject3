# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
#       A = 3; B = 5 -> 243 (3⁵)
#       A = 2; B = 3 -> 8

base = int(input('Введите число: '))
exp = int(input('Введите степень: '))
def power(base, exp):
    if exp == 1:
        return base
    if exp != 1:
        return base * power(base, exp -1)
print('Результат возведения в степень: ', power(base, exp) )

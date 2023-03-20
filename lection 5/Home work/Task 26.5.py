# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
def A_in_b(m, n):
    n -= 1
    while n:
        m *= m
        n -= 1
    print(m)
m = int(input('Enter 1 num: '))
n = int(input('Enter 2 num: '))

A_in_b(m, n)
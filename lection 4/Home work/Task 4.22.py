# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы
# множеств.
from random import randint


first_list = [randint(0, 10) for _ in range(int(input('Введите размер первого набора чисел: ')))]
second_list = [randint(0, 10) for _ in range(int(input('Введите размер второго набора чисел: ')))]

print(first_list, '\n', second_list, sep = '')

count = 0
dci = {}
for i in first_list:
        if i in second_list:
            dci[count] = i
            count += 1
print(dci)
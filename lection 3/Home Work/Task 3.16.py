# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
from random import randint

n = [randint(0, 10) for _ in range(int(input("Enter array's size: ")))]
print(n)

count = 0
x = int(input('Какое число ищем? '))

for i in n:
    if i == x:
        count += 1

print('Число ', x, ' встречалось ', count,' раз(а).')

#task 20

# ang_dict = {"AEIOULNSTRАВЕИНОРСТ": 1, "DGДКЛМПУ": 2,
#             "BCMPБГЁЬЯ": 3, "FHVWYЙЫ": 4, "KЖЗХЦЧ": 5,
#             "JXШЭЮ": 8, "QZФЩЪ": 10}
#
# word = input()
# print(sum([i[1] for i in ang_dict.items() for j in word if j.upper() in i[0]]))


#task 25
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# text = input().split()
# print(text)
# my_dict = {}
#
# for i in text:
#     if i in my_dict:
#         print(f'{i}_{my_dict[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     my_dict[i] = my_dict.get(i, 0) + 1

#   task 27

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте

# text = input().split()
#
# print(len(set(text)))

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)
# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n)

#tassk 332

def fib(n):
    if n in [0, 1]:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(int(input("Enter your num: "))))
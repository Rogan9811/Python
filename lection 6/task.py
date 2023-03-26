from random import randint as rand
# n = int(input("Размер первого массива - "))
# list_1 = []
# for _ in range(0, n):
#     list_1.append(int(input("Элемент массива - ")))

# n = int(input("Размер второго массива - "))
# list_2 = []

# for _ in range(0, n):
#     list_2.append(int(input("Элемент массива - ")))
# print([x for x in list_1 if x not in set(list_2)])

list_0 = [1, 4, 5, 6, 1, 3, 4, 1 ,1 ,5, 5, 6, 9 , 8, 7]

list_1 = list(set(list_0))
print(list_1)
count = 0
for i in range(len(list_1)):
    count += list_0.count(list_1[i])//2
print(count) 
from random import randint
min_num = int(input("Enter min count - "))
max_num = int(input("Enter max count - "))
list_1 = [randint(- 10, 10) for _ in range(int(input("Enter array's size - ")))]
print(list_1)
print([i for i in range(len(list_1)) if max_num >= list_1[i] >= min_num])
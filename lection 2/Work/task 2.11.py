# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1

A = int(input('Enter num: '))
n = 1
result = 0
coll = 0

if A < 0:
    print('Enter right num.')
else:
    while result < A:
        result, n =n, result + n
        coll += 1

    if result == A:
        print(coll)
    else:
        print(-1)
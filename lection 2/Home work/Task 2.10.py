# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
import random as rand

N = int(input('Сколько монеток на столе? введи число: '))
sum_tails = 0
sum_eagle = 0

while N:
    coin = rand.randint(0, 1)
    N -= 1

    if coin == 1:
        sum_tails += 1
    else:
        sum_eagle += 1

print('Орлом вверх лежат ', sum_eagle, ' монеток, а решкой ', sum_tails, ' монеток.')

if sum_eagle > sum_tails:
    print('Нужно переввернуть ', sum_eagle, ' монеток, чтобы они все были повёрнуты орлом вверх.')
else:
    print('Нужно переввернуть ', sum_tails, ' монеток, чтобы они все были повёрнуты решкой вверх.')

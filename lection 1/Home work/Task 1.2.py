# Задача 2: Найдите сумму цифр трехзначного числа.

num = int(input('Enter your num: '))
sum = 0

while num > 0:
    sum += num % 10
    num //= 10

print('Вот сумма ваших цифр в числе: ' + sum)
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

cranes = int(input('Скок журавликов сделали? Введи число: '))

Katya = cranes//3 * 2
Serega = (cranes - Katya)//2
Petya = Serega

print('Катя сделала ', Katya, 'журавликов. Серёга сделал ', Serega, 'журавликов. Петя сделал ', Petya, 'журавликов.')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если
# разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input('Ввдеите длину(в кусочках) шоколадки: '))
m = int(input('Ввдеите ширину(в кусочках) шоколадки: '))
k = int(input('На скок долек поделим эту плитку? Введи число: '))

if k < n * m and ((k % n ==0) or (k % m == 0)):
    print('YESSS')
else:
    print('NOOO')
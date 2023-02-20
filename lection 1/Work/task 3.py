i = int(input('какой вагон по количеству: ')) 
j = int(input('какой вагон по факту: '))


if i == j:
    print('Недостаточно данных.')
else:
    print(i+j-1)
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

Sum = int(input('Enter sum: '))
Mult = int(input('Enter Multi..: '))
count = 0

for i in range(Sum):
    for j in range(Mult):
        if i + j == Sum and i * j == Mult:
            print('Вот загаданные числа: ', i, j)
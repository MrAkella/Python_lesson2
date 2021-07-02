a = input('Введите слова через пробелы: ')
line = a.split(' ')
for num, el in enumerate(line, 1):
    print(num, el [:10])
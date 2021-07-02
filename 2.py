a = input('Введите элементы через запятую: ')
while a.find(',') < 1:
    print('Данные введены некорректно. Попробуйте еще раз!')
    a = input('Введите элементы через запятую: ')
my_list = a.split(',')

print(my_list)
b = len(my_list)
i = 0

while i < (b - 1):
    temp = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = temp
    i += 2

print(my_list)
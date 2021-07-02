list = []
# max = input('Сколько всего элементов будет указано? ')
while True:
    a = input('Введите натуральное число: ')
    if list.count(a) > 0:
        b = list.count(a)
        c = list.index(a)
        list.insert(c + b, a)
        list.sort(reverse=True)
        print(list)
    else:
        list.append(a)
        list.sort(reverse=True)
        print(list)
# искусственная остановка при достижении определенного количества элементов
#    if len(list) == max:
#        break
# print('Итоговый результат: ', list)
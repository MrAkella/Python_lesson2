a = int(input('Введите количество товаров: '))
stuff = []
names = []
prices = []
masses = []
counts = []
catalog = {'Название': names, 'Цена': prices, 'Количество': masses, 'Ед.': counts}
i = 1
while i < (a+1):
    name = input('Введите название товара: ')
    names.append(name)
    price = input('Введите стоимость товара: ')
    prices.append(price)
    mass = input('Введите количество товара: ')
    masses.append(mass)
    count = input('Укажите единицу измерения количества товара: ')
    if counts.count(count) < 1:
        counts.append(count)
    stuff.append((i, {'Название': name, 'Цена': price, 'Количество': mass, 'Ед.': count}))
    i += 1

print('Итоговый перечень товаров:')
for el in stuff:
    print(el)

print('Каталог: ', catalog)
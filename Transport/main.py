while True:
    try:
        a = LandTransport(int(input('Количество колс: ')), input('Цель использования: '), input('Коробка передач: '), input('Марка: '), input('Страна производства: '), input('Тип топлива: '), float(input('Вес(кг): ')), 'red')
        break
    except ValueError:
        print('Неверно ввёл значение атрибутов. Давай попробуем сначала: ')
a.weight_transport()
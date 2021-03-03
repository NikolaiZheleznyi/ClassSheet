from Transport.Transport import Transport
class LandTransport(Transport):
    def __init__(self, number_of_wheels, purpose_of_use, transmission, brand, country_of_origin, engine_type, weight, color):
        Transport.__init__(self, brand, country_of_origin, engine_type, weight, color)
        self.number_of_wheels = number_of_wheels
        self.purpose_of_use = purpose_of_use
        self.transmission = transmission

    def weight_transport(self):
        if 1 < self.number_of_wheels <= 3:
            print('Мотоцикл')
        elif self.number_of_wheels == 4:
            print('Легковой автомобиль')
        elif 4 < self.number_of_wheels:
            print('Грузовой или общественный транспорт')
        else:
            print('У транспорта с отрицательным весом нет категории')

while True:
    try:
        a = LandTransport(int(input('Количество колс: ')), input('Цель использования: '), input('Коробка передач: '), input('Марка: '), input('Страна производства: '), input('Тип топлива: '), float(input('Вес(кг): ')), 'red')
        break
    except ValueError:
        print('Неверно ввёл значение атрибутов. Давай попробуем сначала: ')
a.weight_transport()
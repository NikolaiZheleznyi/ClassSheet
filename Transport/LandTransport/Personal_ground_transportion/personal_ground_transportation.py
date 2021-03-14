from Transport.LandTransport.LandTransport import LandTransport
class Personal_ground_transport(LandTransport):
    def __init__(self, production_date, number_of_wheels, purpose_of_use, transmission,brand, country_of_origin, engine_type, weight, color):
        LandTransport.__init__(self, number_of_wheels, purpose_of_use, transmission, brand, country_of_origin, engine_type, weight, color)
        self.production_date = production_date

    def category_transports(self):
        if 0 < self.weight <= 500:
            print('Транспорт категории А')
        elif 500 < self.weight < 3500:
            print('Транспорт категории B')
        elif 3500 < self.weight:
            print('Транспорт категории C')
        else:
            print('У транспорта с отрицательным весом нет категории')

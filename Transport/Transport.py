class Transport:
    def __init__(self, brand, country_of_origin, engine_type, weight, color):
        self.brand = brand
        self.country_of_origin = country_of_origin
        self.engine_type = engine_type
        self.weight = weight
        self.color = color
    def engine(self):
        if self.engine_type == 'бензин' or 'дизель' or 'газ':
            print('Не экологическое топливо')
        elif self.engine_type == 'электричество':
            print('Экологическое топливо')
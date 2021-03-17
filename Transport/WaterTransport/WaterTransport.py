from Transport.Transport import Transport
class WaterTransport(Transport):
    def __init__(self, brand, country_of_origin, engine_type, weight, color):
        Transport.__init__(self, brand, country_of_origin, engine_type, weight, color)


    def sea_transport(self):
        print('Используется преимущественно в морях')
    def river_transport(self):
        print('Используется преимущественно в реках')
    def ocean_transport(self):
        print('Используется преимущественно в океанах')
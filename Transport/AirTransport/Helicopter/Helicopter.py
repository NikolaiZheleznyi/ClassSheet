from Transport.AirTransport.AirTransport import AirTransport
class Helicopter(AirTransport):
    def __init__(self, brand, country_of_origin, engine_type, weight, color):
        AirTransport.__init__(self, brand, country_of_origin, engine_type, weight, color)


    def helicopter_landing(self):
        print('Техника идёт на посадку')

    def helicopter_take_of(self):
        print('Техника идёт на взлёт')
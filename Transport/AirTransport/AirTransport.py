from Transport.Transport import Transport
class AirTransport(Transport):
    def __init__(self, brand, country_of_origin, engine_type, weight, color):
        Transport.__init__(self, brand, country_of_origin, engine_type, weight, color)


    def take_off(self):
        print('Воздушное судно идёт на взлёт')

    def landing(self):
        print('Воздушное судно идёт на посадку')
from Transport.Transport import Transport
class AirTransport(Transport):
    def __init__(self, type_of_air_tpansport, brand, country_of_origin, engine_type, weight, color):
        Transport.__init__(brand, country_of_origin, engine_type, weight, color)
        self.type_of_air_tpansport = type_of_air_tpansport

    def take_off(self):
        print('Воздушное судно идёт на взлёт')

    def landing(self):
        print('Воздушное судно идёт на посадку')
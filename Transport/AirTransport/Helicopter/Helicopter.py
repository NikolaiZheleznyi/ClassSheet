from Transport.AirTransport.AirTransport import AirTransport
class Helicopter(AirTransport):
    def __init__(self, type_of_helicopter, ype_of_air_tpansport):
        AirTransport.__init__(ype_of_air_tpansport)
        self.type_of_helicopter = type_of_helicopter

    def helicopter_landing(self):
        print('Техника идёт на посадку')

    def helicopter_take_of(self):
        print('Техника идёт на взлёт')
from Transport.AirTransport.AirPlane.Airplane import Airplane
class WarPlane(Airplane):
    def __init__(self, flying_height,brand, country_of_origin, engine_type, weight, color):
        Airplane.__init__(self, flying_height,brand, country_of_origin, engine_type, weight, color)


    def attack(self):
        print('Атаковать противника!')
    def retreat(self):
        print('Уходим, здесь закончили')
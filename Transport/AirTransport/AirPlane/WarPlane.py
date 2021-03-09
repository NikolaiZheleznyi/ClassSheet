from Transport.AirTransport.AirPlane.Airplane import Airplane
class WarPlane(Airplane):
    def __init__(self, arming, flying_height):
        Airplane.__init__(flying_height)
        self.number_of_passengers = arming

    def attack(self):
        print('Атаковать противника!')
    def retreat(self):
        print('Уходим, здесь закончили')
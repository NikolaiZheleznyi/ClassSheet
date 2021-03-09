from Transport.AirTransport.Helicopter.Helicopter import Helicopter
class MilitaryHelicopter(Helicopter):
    def __init__(self, arming, type_of_helicopter):
        Helicopter.__init__(type_of_helicopter)
        self.arming = arming

    def fire_machine_gun(self):
        print('Открыть огонь из пулемёта!')
    def stop_fire_machine_gun(self):
        print('Прекратить огонь из пулемёта!')
    def rocket_fire(self):
        print('Открыть огонь ракетами!')
    def stop_rocket_fire(self):
        print('Прекратить огонь ракетами!')
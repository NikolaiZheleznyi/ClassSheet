from Transport.AirTransport.Helicopter.Helicopter import Helicopter
class MilitaryHelicopter(Helicopter):
    def __init__(self, brand, country_of_origin, engine_type, weight, color):
        Helicopter.__init__(self, brand, country_of_origin, engine_type, weight, color)


    def fire_machine_gun(self):
        print('Открыть огонь из пулемёта!')
    def stop_fire_machine_gun(self):
        print('Прекратить огонь из пулемёта!')
    def rocket_fire(self):
        print('Открыть огонь ракетами!')
    def stop_rocket_fire(self):
        print('Прекратить огонь ракетами!')
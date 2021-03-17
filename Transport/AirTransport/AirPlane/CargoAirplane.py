from Transport.AirTransport.AirPlane.Airplane import Airplane
class CargoAirplane(Airplane):
    def __init__(self, carrying_capacity, flying_height,brand, country_of_origin, engine_type, weight, color):
        Airplane.__init__(self, flying_height,brand, country_of_origin, engine_type, weight, color)
        self.carrying_capacity = carrying_capacity      #грузоподъёмность

    def loading_of_cargo(self):
        print('Груз на борту, капитан!')

    def unloading_of_cargo(self):
        print('Груз покинул нас, капитан!')
from Transport.AirTransport.AirPlane.Airplane import Airplane
class CargoAirplane(Airplane):
    def __init__(self, carrying_capacity, flying_height):
        Airplane.__init__(flying_height)
        self.carrying_capacity = carrying_capacity      #грузоподъёмность
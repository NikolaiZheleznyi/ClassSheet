from Transport.AirTransport.Helicopter.Helicopter import Helicopter
class CargoHelicopter(Helicopter):
    def __init__(self, carrying_capacity, type_of_helicopter):
        Helicopter.__init__(type_of_helicopter)
        self.carrying_capacity = carrying_capacity
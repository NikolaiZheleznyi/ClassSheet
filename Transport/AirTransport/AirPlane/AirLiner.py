from Transport.AirTransport.AirPlane.Airplane import Airplane
class AirLiner(Airplane):
    def __init__(self, number_of_passengers, flying_height):
        Airplane.__init__(flying_height)
        self.number_of_passengers = number_of_passengers
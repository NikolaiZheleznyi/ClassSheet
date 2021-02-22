from Transport.AirTransport.AirPlane.Airplane import Airplane
class WarPlane(Airplane):
    def __init__(self, arming, flying_height):
        Airplane.__init__(flying_height)
        self.number_of_passengers = arming
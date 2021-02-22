from Transport.AirTransport.Helicopter.Helicopter import Helicopter
class MilitaryHelicopter(Helicopter):
    def __init__(self, arming, type_of_helicopter):
        Helicopter.__init__(type_of_helicopter)
        self.arming = arming
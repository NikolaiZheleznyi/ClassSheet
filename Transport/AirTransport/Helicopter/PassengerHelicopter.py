from Transport.AirTransport.Helicopter.Helicopter import Helicopter
class PassengerHelicopter(Helicopter):
    def __init__(self, flight_cost, type_of_helicopter):
        Helicopter.__init__(type_of_helicopter)
        self.flight_cost = flight_cost
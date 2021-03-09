from Transport.AirTransport.Helicopter.Helicopter import Helicopter
class PassengerHelicopter(Helicopter):
    def __init__(self, flight_cost, type_of_helicopter):
        Helicopter.__init__(type_of_helicopter)
        self.flight_cost = flight_cost

    def calculation_flight_price(self):
        print(f"Вы заплатили за {self.flight_cost*5/100} минут полёта")
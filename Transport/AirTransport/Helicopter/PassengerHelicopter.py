from Transport.AirTransport.Helicopter.Helicopter import Helicopter
class PassengerHelicopter(Helicopter):
    def __init__(self, flight_cost, brand, country_of_origin, engine_type, weight, color):
        Helicopter.__init__(self, brand, country_of_origin, engine_type, weight, color)
        self.flight_cost = flight_cost

    def calculation_flight_price(self):
        print(f"Вы заплатили за {self.flight_cost*5/100} минут полёта")
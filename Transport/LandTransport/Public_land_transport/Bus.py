from Transport.LandTransport.Public_land_transport.public_land_transport import Public_land_transport
class Bus(Public_land_transport):
    def __init__(self, place_of_travel, ticket_price, number_of_wheels, purpose_of_use, transmission, brand,
                 country_of_origin, engine_type, weight, color ):
        Public_land_transport.__init__(self, ticket_price, number_of_wheels, purpose_of_use, transmission, brand,
                                       country_of_origin, engine_type, weight, color)
        self.place_of_travel = place_of_travel

    def landing_passenger(self):
        print('Пассажиры вошли в автобус')

    def disembarkation_passenger(self):
        print('Пасажиры покинули автобус')
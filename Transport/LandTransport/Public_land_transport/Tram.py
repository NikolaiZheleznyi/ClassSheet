from Transport.LandTransport.Public_land_transport.public_land_transport import Public_land_transport
class Tram(Public_land_transport):
    def __init__(self, movement_on_rails, ticket_price, number_of_wheels, purpose_of_use, transmission, brand,
                 country_of_origin, engine_type, weight, color ):
        Public_land_transport.__init__(self, ticket_price, number_of_wheels, purpose_of_use, transmission, brand,
                                       country_of_origin, engine_type, weight, color)
        self.movement_on_rails = movement_on_rails # движение по рельсам

    def traffic_rules(self):
        print('Не беспокойся! Трамвай всегда прав;)')
from Transport.LandTransport.Public_land_transport.public_land_transport import Public_land_transport
class Bus(Public_land_transport):
    def __init__(self, place_of_travel, ticket_price ):
        Public_land_transport.__init__(ticket_price)
        self.place_of_travel = place_of_travel
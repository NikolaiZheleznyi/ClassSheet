from Transport.LandTransport.LandTransport import LandTransport
class Public_land_transport(LandTransport):
    def __init__(self, ticket_price, number_of_wheels, purpose_of_use, transmission ):
        LandTransport.__init__(number_of_wheels, purpose_of_use, transmission)
        self.ticket_price = ticket_price

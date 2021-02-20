from Transport.LandTransport.Public_land_transport.public_land_transport import Public_land_transport
class Tram(Public_land_transport):
    def __init__(self, movement_on_rails, ticket_price ):
        Public_land_transport.__init__(ticket_price)
        self.movement_on_rails = movement_on_rails # движение по рельсам
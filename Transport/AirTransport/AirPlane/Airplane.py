from Transport.AirTransport.AirTransport import AirTransport
class Airplane(AirTransport):
    def __init__(self, flying_height,type_of_air_tpansport):
        AirTransport.__init__(type_of_air_tpansport)
        self.flying_height = flying_height
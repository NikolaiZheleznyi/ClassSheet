from Transport.Transport import Transport
class AirTransport(Transport):
    def __init__(self, type_of_air_tpansport, brand, country_of_origin, engine_type, weight, color):
        Transport.__init__(brand, country_of_origin, engine_type, weight, color)
        self.type_of_air_tpansport = type_of_air_tpansport
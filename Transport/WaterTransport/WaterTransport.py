from Transport.Transport import Transport
class WaterTransport(Transport):
    def __init__(self, type_of_water_transport, brand, country_of_origin, engine_type, weight, color  ):
        Transport.__init__(brand, country_of_origin, engine_type, weight, color)
        self.type_of_water_transport = type_of_water_transport
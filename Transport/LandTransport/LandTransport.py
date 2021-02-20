from Transport import Transport
class LandTransport(Transport):
    def __init__(self, number_of_wheels, purpose_of_use, transmission, brand, country_of_origin, engine_type, weight, color  ):
        Transport.__init__(brand, country_of_origin, engine_type, weight, color)
        self.number_of_wheels = number_of_wheels
        self.purpose_of_use = purpose_of_use
        self.transmission = transmission


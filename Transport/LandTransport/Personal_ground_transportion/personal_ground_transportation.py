from Transport.LandTransport.LandTransport import LandTransport
class Personal_ground_transport(LandTransport):
    def __init__(self, production_date, number_of_wheels, purpose_of_use, transmission):
        LandTransport.__init__(number_of_wheels, purpose_of_use, transmission)
        self.production_date = production_date

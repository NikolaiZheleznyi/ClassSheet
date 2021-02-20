from Transport.LandTransport.Personal_ground_transportion.personal_ground_transportation import Personal_ground_transport
class Moterbike(Personal_ground_transport):
    def __init__(self, engine_volume, production_date ):
        Personal_ground_transport.__init__(production_date)
        self.engine_volume = engine_volume

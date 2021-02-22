from Transport.WaterTransport.MilitaryWaterTransport.MilitaryWaterTransport import MilitaryWaterTransport
class AircraftCarrier(MilitaryWaterTransport):
    def __init__(self, number_of_aircraft, range_of_defeat):
        MilitaryWaterTransport.__init__(range_of_defeat)
        self.number_of_aircraft = number_of_aircraft
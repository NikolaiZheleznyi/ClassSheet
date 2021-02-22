from Transport.WaterTransport.WaterTransport import WaterTransport
class MilitaryWaterTransport(WaterTransport):
    def __init__(self, range_of_defeat, type_of_water_transport):
        WaterTransport.__init__(type_of_water_transport)
        self.range_of_defeat = range_of_defeat
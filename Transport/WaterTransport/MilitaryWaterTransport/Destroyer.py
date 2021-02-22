from Transport.WaterTransport.MilitaryWaterTransport.MilitaryWaterTransport import MilitaryWaterTransport
class Destroyer(MilitaryWaterTransport):
    def __init__(self, number_of_guns, range_of_defeat):
        MilitaryWaterTransport.__init__(range_of_defeat)
        self.number_of_guns = number_of_guns
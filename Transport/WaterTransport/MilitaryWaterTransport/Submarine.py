from Transport.WaterTransport.MilitaryWaterTransport.MilitaryWaterTransport import MilitaryWaterTransport
class Submarine(MilitaryWaterTransport):
    def __init__(self, immersion_depth, range_of_defeat):
        MilitaryWaterTransport.__init__(range_of_defeat)
        self.immersion_depth = immersion_depth   #глубина погружения

    def immersion(self):
        print(f'Погружаемся на глубину {self.immersion_depth} метров')
    def float_up_(self):
        print('Всплываем!')
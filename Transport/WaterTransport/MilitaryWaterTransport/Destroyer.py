from Transport.WaterTransport.MilitaryWaterTransport.MilitaryWaterTransport import MilitaryWaterTransport
class Destroyer(MilitaryWaterTransport):
    def __init__(self, number_of_guns, range_of_defeat):
        MilitaryWaterTransport.__init__(range_of_defeat)
        self.number_of_guns = number_of_guns

    def fire_guns(self):
        print(f'Огонь из всех {self.number_of_guns} орудий!')

    def stop_fire_guns(self):
        print('Прекратить огонь!')
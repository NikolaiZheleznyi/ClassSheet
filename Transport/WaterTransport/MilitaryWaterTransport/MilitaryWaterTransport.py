from Transport.WaterTransport.WaterTransport import WaterTransport
class MilitaryWaterTransport(WaterTransport):
    def __init__(self, range_of_defeat, type_of_water_transport):
        WaterTransport.__init__(type_of_water_transport)
        self.range_of_defeat = range_of_defeat

    def computation_hits_or_not(self):
        if self.range_of_defeat < 500:
            print(f'К сожалению, ты выстрелил на {self.range_of_defeat} метров, тебе не хватило до цели {500 - self.range_of_defeat} метров')
        elif self.range_of_defeat > 500:
            print('Поздравляю, ты поразил цель!')
        else:
            print('Что-то ты не то написал, ничего не получится')
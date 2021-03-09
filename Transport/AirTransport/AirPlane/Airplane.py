from Transport.AirTransport.AirTransport import AirTransport
class Airplane(AirTransport):
    def __init__(self, flying_height,type_of_air_tpansport):
        AirTransport.__init__(type_of_air_tpansport)
        self.flying_height = flying_height

    def air_company(self):
        if 0 < self.flying_height < 10000:
            print('На этой высоте могут летать как пассажирские, грузовые самолёты, так и военные самолёты')
        elif self.flying_height == 12000:
            print('Максимальная высота полёта грузового самолёта')
        elif self.flying_height == 17000:
            print('Максимальная высота полёта военного самолёта')
        else:
            print('Выше 17000 м самолёты не любят летать. Если ты ввел дугое значение, то подумай, что ты делаешь.')
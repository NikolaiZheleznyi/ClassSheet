from Transport.AirTransport.AirTransport import AirTransport
class Airplane(AirTransport):
    def __init__(self, flying_height,brand, country_of_origin, engine_type, weight, color):
        AirTransport.__init__(self, brand, country_of_origin, engine_type, weight, color)
        self.flying_height = flying_height

    def air_company(self):
        if 0 < self.flying_height < 10000:
            print('На этой высоте могут летать как пассажирские, грузовые самолёты, так и военные самолёты')
        elif 10000 < self.flying_height < 12000:
            print('На этой высоте могут летать грузовые самолёты, так и военные самолёты')
        elif 12000 < self.flying_height < 17000:
            print('На этой высоте могут летать военные самолёты')
        else:
            print('Выше 17000 м самолёты не любят летать. Если ты ввел дугое значение, то подумай, что ты делаешь.')
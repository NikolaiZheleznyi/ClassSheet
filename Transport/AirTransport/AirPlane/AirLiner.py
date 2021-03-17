from Transport.AirTransport.AirPlane.Airplane import Airplane
class AirLiner(Airplane):
    def __init__(self, range_of_flight, flying_height,brand, country_of_origin, engine_type, weight, color):
        Airplane.__init__(self, flying_height,brand, country_of_origin, engine_type, weight, color)
        self.range_of_flight = range_of_flight

    def range_of_flight_air_liner(self):
        if 0 < self.range_of_flight <= 1000:
            print('Самолёты местных воздушных линий')
        elif 1000 < self.range_of_flight <= 2500:
            print('Ближнемагистральные самолёты')
        elif 2500 < self.range_of_flight <= 6000:
            print('Средемагистральные самолёты')
        elif self.range_of_flight > 6000:
            print('Дальнемагистральные самолёты')
        else:
            print('Что-то ты не те значения вводишь')
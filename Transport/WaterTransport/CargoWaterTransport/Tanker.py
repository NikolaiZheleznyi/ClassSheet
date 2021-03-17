from Transport.WaterTransport.CargoWaterTransport.CargoWaterTransport import CargoWaterTransport
from datetime import timedelta, datetime
class Tanker(CargoWaterTransport):
    def __init__(self, destination,brand, country_of_origin, engine_type, weight, color):
        CargoWaterTransport.__init__(self, brand, country_of_origin, engine_type, weight, color)
        self.destination = destination #пункт назначения

    def distance_of_destination(self):
        time_to_goal = datetime.now() - timedelta(15)
        print(f'Корабль придёт в {self.destination} через 15 дней. {time_to_goal}')
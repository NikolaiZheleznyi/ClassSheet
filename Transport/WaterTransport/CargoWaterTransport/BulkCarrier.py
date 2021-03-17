from Transport.WaterTransport.CargoWaterTransport.CargoWaterTransport import CargoWaterTransport
from datetime import timedelta, datetime
class BulkCarrier(CargoWaterTransport):
    def __init__(self, destination, brand, country_of_origin, engine_type, weight, color ):
        CargoWaterTransport.__init__(self, brand, country_of_origin, engine_type, weight, color)
        self.destination = destination #пункт назначения

    def distance_of_destination(self):
        time_to_goal = datetime.now() + timedelta(2)
        print(f'Корабль придёт в {self.destination} через 2 дня. {time_to_goal}')
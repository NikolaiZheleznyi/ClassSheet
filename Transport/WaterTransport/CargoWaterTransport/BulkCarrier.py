from Transport.WaterTransport.CargoWaterTransport.CargoWaterTransport import CargoWaterTransport
from datetime import timedelta, datetime
class BulkCarrier(CargoWaterTransport):
    def __init__(self, destination,type_of_cargo, time_to_goal):
        CargoWaterTransport.__init__(type_of_cargo)
        self.destination = destination #пункт назначения
        self.time_to_goal = time_to_goal
    def distance_of_destination(self):
        self.time_to_goal = datetime.now() - timedelta(2)
        print(f'Корабль придёт в {self.destination} через 2 дня. {self.time_to_goal}')
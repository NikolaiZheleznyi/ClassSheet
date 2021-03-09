from Transport.WaterTransport.CargoWaterTransport.CargoWaterTransport import CargoWaterTransport
from datetime import timedelta, datetime
class Tanker(CargoWaterTransport):
    def __init__(self, destination,type_of_cargo,time_to_goal):
        CargoWaterTransport.__init__(type_of_cargo)
        self.destination = destination #пункт назначения
        self.time_to_goal = time_to_goal

    def distance_of_destination(self):
        self.time_to_goal = datetime.now() - timedelta(15)
        print(f'Корабль придёт в {self.destination} через 15 дней. {self.time_to_goal}')
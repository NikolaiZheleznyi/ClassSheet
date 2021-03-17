from Transport.AirTransport.Helicopter.Helicopter import Helicopter
class CargoHelicopter(Helicopter):
    def __init__(self, carrying_capacity, brand, country_of_origin, engine_type, weight, color):
        Helicopter.__init__(self, brand, country_of_origin, engine_type, weight, color)
        self.carrying_capacity = carrying_capacity # грузоподъёмность

    def carrying_capacity_helicopter(self):
        if 0 < self.carrying_capacity <= 5:
            print(f' Вертолёт малой грузоподъёмности. Его грузоподъёмность составляет {self.carrying_capacity} тон')
        elif 5 < self.carrying_capacity < 10:
            print(f' Вертолёт средней грузоподъёмности. Его грузоподъёмность составляет {self.carrying_capacity} тон')
        elif self.carrying_capacity > 10:
            print(f' Вертолёт большой грузоподъёмности. Его грузоподъёмность составляет {self.carrying_capacity} тон')
        else:
            print(f'{self.carrying_capacity} - не верное значение грузоподъёмности')
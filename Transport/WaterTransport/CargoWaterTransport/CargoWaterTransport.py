from Transport.WaterTransport.WaterTransport import WaterTransport
class CargoWaterTransport(WaterTransport):
    def __init__(self, type_of_cargo, type_of_water_transport):
        WaterTransport.__init__(type_of_water_transport)
        self.type_of_cargo = type_of_cargo

    def loading_cargo_on_ship(self):
        print('Погрузка завершена! Корабаль готов к отправлению!')

    def unloading_cargo_on_ship(self):
        print('Разгрузка завершена!\nТеперь можно и отдохнуть')
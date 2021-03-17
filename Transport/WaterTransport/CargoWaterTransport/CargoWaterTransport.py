from Transport.WaterTransport.WaterTransport import WaterTransport
class CargoWaterTransport(WaterTransport):
    def __init__(self, brand, country_of_origin, engine_type, weight, color):
        WaterTransport.__init__(self, brand, country_of_origin, engine_type, weight, color)


    def loading_cargo_on_ship(self):
        print('Погрузка завершена! Корабаль готов к отправлению!')

    def unloading_cargo_on_ship(self):
        print('Разгрузка завершена!\nТеперь можно и отдохнуть')
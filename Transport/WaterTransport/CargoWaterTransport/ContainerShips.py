from Transport.WaterTransport.CargoWaterTransport.CargoWaterTransport import CargoWaterTransport
class ContainerShips(CargoWaterTransport):
    def __init__(self, destination,type_of_cargo):
        CargoWaterTransport.__init__(type_of_cargo)
        self.destination = destination #пункт назначения
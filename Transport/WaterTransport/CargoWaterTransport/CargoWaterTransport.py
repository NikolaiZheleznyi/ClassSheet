from Transport.WaterTransport.WaterTransport import WaterTransport
class CargoWaterTransport(WaterTransport):
    def __init__(self, type_of_cargo, type_of_water_transport):
        WaterTransport.__init__(type_of_water_transport)
        self.type_of_cargo = type_of_cargo
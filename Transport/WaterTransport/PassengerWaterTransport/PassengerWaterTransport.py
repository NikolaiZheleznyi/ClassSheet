from Transport.WaterTransport.WaterTransport import WaterTransport
class PassengerWaterTransport(WaterTransport):
    def __init__(self, number_of_passengers, type_of_water_transport):
        WaterTransport.__init__(type_of_water_transport)
        self.number_of_passengers = number_of_passengers

    def loading_passengers(self):
        print('Все на борт!')

    def unloading_passengers(self):
        print('Покинуть водное судно!')
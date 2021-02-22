from Transport.WaterTransport.PassengerWaterTransport.PassengerWaterTransport import PassengerWaterTransport
class Powerboat(PassengerWaterTransport):
    def __init__(self, type_of_powerboat, number_of_passengers):
        PassengerWaterTransport.__init__(number_of_passengers)
        self.type_of_powerboat = type_of_powerboat
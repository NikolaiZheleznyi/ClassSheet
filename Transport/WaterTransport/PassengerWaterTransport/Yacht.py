from Transport.WaterTransport.PassengerWaterTransport.PassengerWaterTransport import PassengerWaterTransport
class Yacht(PassengerWaterTransport):
    def __init__(self, yacht_length, number_of_passengers):
        PassengerWaterTransport.__init__(number_of_passengers)
        self.yacht_length = yacht_length
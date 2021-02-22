from Transport.WaterTransport.PassengerWaterTransport.PassengerWaterTransport import PassengerWaterTransport
class CruiseShip(PassengerWaterTransport):
    def __init__(self, number_of_decks, number_of_passengers):
        PassengerWaterTransport.__init__(number_of_passengers)
        self.number_of_decks = number_of_decks
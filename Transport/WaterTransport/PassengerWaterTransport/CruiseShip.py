from Transport.WaterTransport.PassengerWaterTransport.PassengerWaterTransport import PassengerWaterTransport
class CruiseShip(PassengerWaterTransport):
    def __init__(self, number_of_decks, number_of_passengers):
        PassengerWaterTransport.__init__(number_of_passengers)
        self.number_of_decks = number_of_decks

    def deck_cost(self):
        if self.number_of_decks < 3:
            print('Малый круизный корабль')
        elif 2 < self.number_of_decks <= 5:
            print('Средний круизный корабль')
        elif self.number_of_decks > 5:
            print('Большой круизный корабль')
        else:
            print('Неверные данные значения ввёл, дружок')
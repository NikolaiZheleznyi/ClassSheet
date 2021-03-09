from Transport.WaterTransport.PassengerWaterTransport.PassengerWaterTransport import PassengerWaterTransport
class Powerboat(PassengerWaterTransport):
    def __init__(self, type_of_powerboat, number_of_passengers):
        PassengerWaterTransport.__init__(number_of_passengers)
        self.type_of_powerboat = type_of_powerboat

    def start_the_motor(self):
        print(f'Завести мотор! Как и всегда, {self.type_of_powerboat} работает отлично')

    def stop_the_motor(self):
        print(f'Заглушить мотор! Сейчас {self.type_of_powerboat} будет остывать')

    def calculation_number_of_seats(self):
        if 5 - self.number_of_passengers >= 0:
            print(f'Отличные новости! {self.number_of_passengers} пассажиров поместились на наш катер!')
        elif 5 - self.number_of_passengers < 0:
            print(f'Плохие новости! {self.number_of_passengers} пассажиров не могут поместиться на наш катер!')
        else:
            print('Дружок, надо вводить цифры, по-другому не работает!')
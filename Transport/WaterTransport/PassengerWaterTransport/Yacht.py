from Transport.WaterTransport.PassengerWaterTransport.PassengerWaterTransport import PassengerWaterTransport
class Yacht(PassengerWaterTransport):
    def __init__(self, yacht_length, number_of_passengers):
        PassengerWaterTransport.__init__(number_of_passengers)
        self.yacht_length = yacht_length

    def start_yacht_paty(self):
        print(f'Начинаем вечеринку!! Вся яхта, длинной {self.yacht_length}, метров в твоём распоряжении')

    def stop_yacht_paty(self):
        print(f'Ну всё, конец тусовке. {self.number_of_passengers} человек покинули яхту.')
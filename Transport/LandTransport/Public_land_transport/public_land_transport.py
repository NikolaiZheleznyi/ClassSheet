from Transport.LandTransport.LandTransport import LandTransport
class Public_land_transport(LandTransport):
    def __init__(self, ticket_price, number_of_wheels, purpose_of_use, transmission):
        LandTransport.__init__(self, number_of_wheels, purpose_of_use, transmission)
        self.ticket_price = ticket_price
    def ticket(self):
        if 0 < self.ticket_price < 1:
            print('Льготный билет')
        elif self.ticket_price > 1:
            print('Стандартный билет')
        else:
            print('Цена указана не верно')
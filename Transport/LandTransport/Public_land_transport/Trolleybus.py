from Transport.LandTransport.Public_land_transport.public_land_transport import Public_land_transport
class Trolleybus(Public_land_transport):
    def __init__(self, type_pantograph, ticket_price, number_of_wheels, purpose_of_use, transmission, brand,
                 country_of_origin, engine_type, weight, color):
        Public_land_transport.__init__(self, ticket_price, number_of_wheels, purpose_of_use, transmission, brand,
                                       country_of_origin, engine_type, weight, color)
        self.type_pantograph = type_pantograph  #  тип токоприёмника

    def checking_the_pantograph(self):
        print('Не беспокойтесь! Все системы проверенны. Проблем с подачей энергии не будет!')
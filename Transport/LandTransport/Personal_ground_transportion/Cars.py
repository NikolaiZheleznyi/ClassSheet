from Transport.LandTransport.Personal_ground_transportion.personal_ground_transportation import Personal_ground_transport

class Cars(Personal_ground_transport):
    def __init__(self, car_type, number_of_doors, production_date ):
        Personal_ground_transport.__init__(production_date)
        self.car_type = car_type
        self.number_of_doors = number_of_doors

    def transportation_children(self):
        print('Детское кресло установленно. Приятной поездки')



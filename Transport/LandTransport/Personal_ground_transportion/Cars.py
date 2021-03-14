from Transport.LandTransport.Personal_ground_transportion.personal_ground_transportation import Personal_ground_transport

class Cars(Personal_ground_transport):
    def __init__(self, car_type, production_date, number_of_wheels, purpose_of_use, transmission,brand, country_of_origin, engine_type, weight, color):
        Personal_ground_transport.__init__(self, production_date, number_of_wheels, purpose_of_use, transmission,brand, country_of_origin, engine_type, weight, color)
        self.car_type = car_type


    def transportation_children(self):
        print('Детское кресло установленно. Приятной поездки')



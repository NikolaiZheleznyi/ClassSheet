from Transport.LandTransport.Personal_ground_transportion.personal_ground_transportation import Personal_ground_transport
class Moterbike(Personal_ground_transport):
    def __init__(self, engine_volume, production_date, number_of_wheels, purpose_of_use, transmission, brand, country_of_origin, engine_type, weight, color ):
        Personal_ground_transport.__init__(self, production_date, number_of_wheels, purpose_of_use, transmission, brand, country_of_origin, engine_type, weight, color)
        self.engine_volume = engine_volume

    def use_helmet(self):
        choice_of_action = int(input('Чтобы надеть шлем нажмите 1 \nЧтобы снять шлем нажмите 2 \nВаше действие: '))
        if choice_of_action == 1:
            print('Теперь шмел сжимает голову водителю, но он в безопасности благодаря вам')
        elif choice_of_action == 2:
            print('Если водитель был в шлеме, то теперь он без него. А если он был без шлема, то ты зря растрачиваешь потенциал этой программы :( ')
        else:
            print('Ты должен был ввести 1 или 2, других вариантов нет, такая вот вседозволенность')

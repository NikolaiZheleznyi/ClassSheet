#from Transport.LandTransport.Personal_ground_transportion.personal_ground_transportation import Personal_ground_transport
class Moterbike(Personal_ground_transport):
    def __init__(self, engine_volume, choice_of_action #, production_date ):
        #Personal_ground_transport.__init__(production_date)
        self.engine_volume = engine_volume
        self.choice_of_action = choice_of_action
    def use_helmet(self):
        self.choice_of_action = int(input('Чтобы надеть шлем нажмите 1 \nЧтобы снять шлем нажмите 2 \nВаше действие: '))
        if self.choice_of_action == 1:
            print('Теперь шмел сжимает голову водителю, но он в безопасности благодаря вам')
        elif self.choice_of_action == 2:
            print('Если водитель был в шлеме, то теперь он без него. А если он был без шлема, то ты зря растрачиваешь потенциал этой программы :( ')
        else:
            print('Ты должен был ввести 1 или 2, других вариантов нет, такая вот вседозволенность')

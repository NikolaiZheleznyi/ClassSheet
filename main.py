from Transport.Transport import Transport
from Transport.LandTransport.LandTransport import LandTransport
from Transport.LandTransport.Public_land_transport.public_land_transport import Public_land_transport
from Transport.LandTransport.Public_land_transport.Tram import Tram
from Transport.LandTransport.Public_land_transport.Bus import Bus
from Transport.LandTransport.Public_land_transport.Trolleybus import Trolleybus
from Transport.LandTransport.Personal_ground_transportion.personal_ground_transportation import Personal_ground_transport
from Transport.LandTransport.Personal_ground_transportion.Moterbike import Moterbike
from Transport.LandTransport.Personal_ground_transportion.Cars import Cars
from Transport.WaterTransport.WaterTransport import WaterTransport
from Transport.WaterTransport.PassengerWaterTransport.PassengerWaterTransport import PassengerWaterTransport
from Transport.WaterTransport.PassengerWaterTransport.Yacht import Yacht
from Transport.WaterTransport.PassengerWaterTransport.Powerboat import Powerboat
from Transport.WaterTransport.PassengerWaterTransport.CruiseShip import CruiseShip
from Transport.WaterTransport.MilitaryWaterTransport.MilitaryWaterTransport import MilitaryWaterTransport
from Transport.WaterTransport.MilitaryWaterTransport.Submarine import Submarine
from Transport.WaterTransport.MilitaryWaterTransport.Destroyer import Destroyer
from Transport.WaterTransport.MilitaryWaterTransport.AircraftCarrier import AircraftCarrier
from Transport.WaterTransport.CargoWaterTransport.CargoWaterTransport import CargoWaterTransport
from Transport.WaterTransport.CargoWaterTransport.Tanker import Tanker
from Transport.WaterTransport.CargoWaterTransport.BulkCarrier import BulkCarrier
from Transport.WaterTransport.CargoWaterTransport.ContainerShips import ContainerShips
from Transport.AirTransport.AirTransport import AirTransport
from Transport.AirTransport.AirPlane.Airplane import Airplane
from Transport.AirTransport.AirPlane.WarPlane import WarPlane
from Transport.AirTransport.AirPlane.AirLiner import AirLiner
from Transport.AirTransport.AirPlane.CargoAirplane import CargoAirplane
from Transport.AirTransport.Helicopter.Helicopter import Helicopter
from Transport.AirTransport.Helicopter.MilitaryHelicopter import MilitaryHelicopter
from Transport.AirTransport.Helicopter.CargoHelicopter import CargoHelicopter
from Transport.AirTransport.Helicopter.PassengerHelicopter import PassengerHelicopter
from datetime import datetime,timedelta
while True:
    type_main = int(input('Чтовы выбрать Транспорт нажмите 1\n'
                          'Чтобы выбрать раздел наземный транспорт нажмите 2\n'
                          'Чтобы выбрать раздел воздушный транспорт нажмите 3\n'
                          'Чтобы выбрать раздел водный транспорт нажмите 4\n'
                          'Введите цифру:  '))


    if type_main == 1:


        def menu_transport():
            while True:
                try:
                    transport = Transport(input('Марка: '), input('Страна производства: '),
                                          input('Тип топлива (бензин, газ, дизель, электричество): '),
                                          int(input('Вес техники: ')), input('Цвет кузова: '))
                    break
                except ValueError:
                    print('Неверно ввёл значение атрибутов. Давай попробуем сначала: ')

            while True:
                try:
                    type_transport = int(input('Чтобы проверить топливо на экологичность введите цифру 1\n'
                                               'Чтобы пропустить введите цифру 2\n'
                                               'Введите цифру: '))
                    if type_transport == 1:
                        transport.engine()
                        break
                    elif type_transport == 2:
                        break
                    else:
                        print('Попробуй еще раз')
                except ValueError:
                    print('Попробуй еще раз')
        menu_transport()


    elif type_main == 2:


        def menu_land_transport():
            while True:
                try:
                    land_transport = LandTransport(int(input('Количество колс: ')),'personal',
                                                   'automat', 'bmw', 'germany',
                                                   'disel',3000, 'red')
                    break
                except ValueError:
                    print('Неверно ввёл значение атрибутов. Давай попробуем сначала: ')

            while True:
                try:
                    type_number_of_wheels_transport = int(input('Чтобы определить тип транспорта введите цифру 1\n'
                                     'Чтобы продолжить введите цифру 2\n'
                                     'Введите цифру: '))
                    if type_number_of_wheels_transport == 1:
                        land_transport.number_of_wheels_transport()
                        break
                    elif type_number_of_wheels_transport == 2:
                        break
                    else:
                        print('Попробуй еще раз')
                except ValueError:
                    print('Попробуй еще раз')
        menu_land_transport()

        while True:
            type_land_transport = int(input('Чтобы выбрать личный транспорт нажмите 1\n'
                                            'Чтобы выбрать общественный транспорт нажмите 2\n'
                                            'Введите цифру: '))
            if type_land_transport == 1:

                def personal_transport():

                    while True:
                        try:
                            personal_transport = Personal_ground_transport(2017, '2 or 4', 'personal', 'automat','bmw', 'germany',
                                                                           'disel', int(input('Введите вес техники (кг): ')), 'черный')
                            break
                        except ValueError:
                            print('Неверно ввёл значение атрибутов. Давай попробуем сначала: ')

                    while True:
                        try:
                            type_category_transports = int(input('Чтобы определить категорию транспорта введите цифру 1\n'
                                                                    'Чтобы продолжить введите цифру 2\n'
                                                                    'Введите цифру: '))
                            if type_category_transports == 1:
                                personal_transport.category_transports()
                                break

                            elif type_category_transports == 2:
                                break

                            else:
                                print('Попробуй еще раз')
                        except ValueError:
                            print('Попробуй еще раз')
                    while True:
                            type_personal_transport = int(input('Чтобы выбрать Автомобиль введите цифру 1\n'
                                                                    'Чтобы выбрать Мотоцикл введите цифру 2\n'
                                                                    'Чтобы завершить работу нажмите 3\n'
                                                                    'Введите цифру: '))
                            if type_personal_transport == 1:
                                cars = Cars('car_type', 'production_date', 'number_of_wheels', 'purpose_of_use',
                                            'transmission,brand', 'country_of_origin', 'engine_type', 'weight', 1, 1)

                                type_transportation_children = int(input(' Чтобы установить детское кресло введите цифру 1\n'
                                                                                     'Чтобы завершить программу введите цифру 2\n'
                                                                                     'Введите цифру: '))
                                if type_transportation_children == 1:
                                        cars.transportation_children()
                                        break
                                else:
                                    break

                            elif type_personal_transport == 2:
                                motobike = Moterbike('engine_volume', 'production_date', 'number_of_wheels', 'purpose_of_use',
                                                     'transmission', 'brand', 'country_of_origin', 'engine_type', 'weight', 'color')
                                type_use_helmet = int(input('Чтобы сесть на мотоцикл введите цифру 1\n'
                                                                                     'Чтобы завершить программу введите цифру 2\n'
                                                                                     'Введите цифру: '))
                                if type_use_helmet == 1:
                                        motobike.use_helmet()
                                        break
                                else:
                                    break
                            elif type_personal_transport == 3:
                                break
                personal_transport()
            elif type_land_transport == 2:

                def public_transport():

                    while True:
                        try:
                            publicTransport = Public_land_transport(int(input('Сколько вы заплатили за билет?\nВведите число: ')),
                                                                    'number_of_wheels', 'purpose_of_use', 'transmission', 'brand',
                                                                    'country_of_origin', 'engine_type', 'weight', 'color')
                            break
                        except ValueError:
                            print('Неверно ввёл значение атрибутов. Давай попробуем сначала: ')

                    while True:
                        try:
                            type_ticket = int(
                                input('Чтобы узнать какой у вас билет введите цифру 1\n'
                                      'Чтобы продолжить введите цифру 2\n'
                                      'Введите цифру: '))
                            if type_ticket == 1:
                                publicTransport.ticket()
                                break

                            elif type_ticket == 2:
                                break

                            else:
                                print('Попробуй еще раз')
                        except ValueError:
                            print('Попробуй еще раз')
                    while True:
                            type_public_transport = int(input('Чтобы выбрать Трамвай введите цифру 1\n'
                                                                    'Чтобы выбрать Автобус введите цифру 2\n'
                                                                    'Чтобы выбрать Троллейбус нажмите 3\n'
                                                                    'Чтобы завершить работу нажмите 4\n'
                                                                    'Введите цифру: '))
                            if type_public_transport == 1:
                                trams = Tram('car_type', 'production_date', 'number_of_wheels', 'purpose_of_use',
                                            'transmission,brand', 'country_of_origin', 'engine_type', 'weight', 1, 1)

                                type_traffic_rules = int(input(' Чтобы узнать права трамвая на дороге введите цифру 1\n'
                                                                                     'Чтобы завершить программу введите цифру 2\n'
                                                                                     'Введите цифру: '))
                                if type_traffic_rules == 1:
                                        trams.traffic_rules()
                                        break
                                else:
                                    break

                            elif type_public_transport == 2:
                                bus = Bus('engine_volume', 'production_date', 'number_of_wheels', 'purpose_of_use',
                                          'transmission', 'brand', 'country_of_origin', 'engine_type', 'weight', 'color')
                                type_landing_pasangers = int(input('Чтобы загрузить пассажиров в автобус введите цифру 1\n'
                                                                   'Чтобы высадить паасажиров из автобуса введите цифру 2\n'
                                                                    'Чтобы завершить программу введите цифру 3\n'
                                                                     'Введите цифру: '))
                                if type_landing_pasangers == 1:
                                        bus.landing_passenger()
                                        break
                                elif type_landing_pasangers == 2:
                                    bus.disembarkation_passenger()
                                    break
                                else:
                                    break
                            elif type_public_transport == 3:
                                trolleybus = Trolleybus('car_type', 'production_date', 'number_of_wheels', 'purpose_of_use',
                                             'transmission,brand', 'country_of_origin', 'engine_type', 'weight', 1, 1)

                                type_checking = int(input(' Чтобы проверить контакт с электричеством введите цифру 1\n'
                                                               'Чтобы завершить программу введите цифру 2\n'
                                                               'Введите цифру: '))
                                if type_checking == 1:
                                    trolleybus.checking_the_pantograph()
                                    break
                                else:
                                    break



                public_transport()

                break


    elif type_main == 3:


        def menu_air_transport():
            air_transport = AirTransport('brand', 'country_of_origin', 'engine_type', 'weight', 'color')

            while True:
                try:
                    type_landing = int(input('Чтобы поднять судно в воздух введите цифру 1\n'
                                             'Чтобы посадить посадить судно введите цифру 2\n'
                                             'Введите цифру: '))
                    if type_landing == 1:
                        air_transport.take_off()
                        break
                    elif type_landing == 2:
                        air_transport.landing()
                        break
                    else:
                        print('Нет такого варинта ввода')
                except ValueError:
                    print('Попробуй еще раз')
        menu_air_transport()


        type_air_transport = int(input('Чтобы выбрать самолёт нажмите 1\n'
                                        'Чтобы выбрать вертолёт нажмите 2\n'
                                        'Введите цифру: '))
        if type_air_transport == 1:

            def airplane():
                airplane = Airplane(int(input('Введите высоту полёта: ')),'brand', 'country_of_origin', 'engine_type', 'weight', 'color')

                while True:
                    try:
                        type_air_company = int(input('Чтобы определить тип воздушного транспорта введите цифру 1\n'
                                                     'Чтобы продолжить введите цифру 2\n'
                                                     'Введите цифру: '))
                        if type_air_company == 1:
                            airplane.air_company()
                            break

                        elif type_air_company == 2:
                            break

                        else:
                            print('Попробуй еще раз')
                    except ValueError:
                        print('Попробуй еще раз')
                while True:
                    type_airplane = int(input('Чтобы выбрать пассажирский самолёт введите цифру 1\n'
                                                'Чтобы выбрать грузовой самолёт введите цифру 2\n'
                                                'Чтобы выбрать военный самолёт нажмите 3\n'
                                                'Чтобы завершить работу нажмите 4\n'
                                                'Введите цифру: '))
                    if type_airplane == 1:

                        airliner = AirLiner(int(input('Введите дальность полёта (м): ')),'flying_height','brand',
                                                        'country_of_origin', 'engine_type', 'weight', 'color')

                        type_range_of_flight = int(input(' Чтобы узнать тип самолёта введите цифру 1\n'
                                                            'Чтобы завершить программу введите цифру 2\n'
                                                            'Введите цифру: '))
                        if type_range_of_flight == 1:
                            airliner.range_of_flight_air_liner()
                            break
                        else:
                            break

                    elif type_airplane == 2:

                        cargoAirplane = CargoAirplane('carrying_capacity', 'flying_height','brand', 'country_of_origin',
                                                      'engine_type', 'weight', 'color')
                        type_loading_cargo = int(input('Чтобы произвести загрузку груза введите цифру 1\n'
                                                    'Чтобы произвести выгрузку груза введите цифру 2\n'
                                                    'Введите цифру: '))
                        if type_loading_cargo == 1:
                            cargoAirplane.loading_of_cargo()
                            break
                        elif type_loading_cargo == 2:
                            cargoAirplane.unloading_of_cargo()
                        else:
                            print('Нет такого варианта')

                    elif type_airplane == 3:

                        warplane = WarPlane('flying_height', 'brand',
                                                      'country_of_origin',
                                                      'engine_type', 'weight', 'color')
                        type_attack = int(input('Чтобы атаковать противника введите цифру 1\n'
                                                'Чтобы прекратить атаку введите цифру 2\n'
                                                'Введите цифру: '))
                        if type_attack == 1:
                            warplane.attack()
                            break
                        elif type_attack == 2:
                            warplane.retreat()
                        else:
                            print('Нет такого варианта')
                        break
            airplane()
        elif type_air_transport == 2:

            def helicopter():
                helicopter = Helicopter('brand', 'country_of_origin', 'engine_type', 'weight', 'color')

                while True:
                    try:
                        type_helocopter_landing = int(input('Чтобы посадить вертолёт на поверхность введите цифру 1\n'
                                                            'Чтобы поднять вертолёт в воздух введите цифру 2\n'
                                                            'Введите цифру: '))
                        if type_helocopter_landing == 1:
                            helicopter.helicopter_landing()
                            break

                        elif type_helocopter_landing == 2:
                            helicopter.helicopter_take_of()
                            break

                        else:
                            print('Попробуй еще раз')
                    except ValueError:
                        print('Попробуй еще раз')
                while True:
                        type_Helicopter = int(input('Чтобы выбрать грузовой вертолёт введите цифру 1\n'
                                                                'Чтобы выбрать военный вертолёт введите цифру 2\n'
                                                                'Чтобы выбрать пассажирский вертолёт нажмите 3\n'
                                                                'Чтобы завершить работу нажмите 4\n'
                                                                'Введите цифру: '))
                        if type_Helicopter == 1:
                            cargo_helicopter = CargoHelicopter(int(input('Введите максимальную грузоподъёмность вертолёта (т): ')),
                                                               'brand', 'country_of_origin', 'engine_type', 'weight', 'color')

                            type_carrying_capacity = int(input(' Чтобы определить тип вертолёта по грузоподъёмности введите цифру 1\n'
                                                                 'Чтобы завершить программу введите цифру 2\n'
                                                                 'Введите цифру: '))
                            if type_carrying_capacity == 1:
                                    cargo_helicopter.carrying_capacity_helicopter()
                                    break
                            else:
                                break

                        elif type_Helicopter== 2:
                            warHelicopter = MilitaryHelicopter('brand', 'country_of_origin', 'engine_type', 'weight', 'color')
                            type_fire = int(input('Чтобы атаковать из пулемёта введите цифру 1\n'
                                                   'Чтобы прекратить атаку из пулемёта введите цифру 2\n'
                                                   'Чтобы атаковать ракетой введите цифру 3\n'
                                                   'Чтобы прекратить атаку ракетой введите цифру 4\n'
                                                   'Чтобы завершить программу введите цифру 5\n'
                                                   'Введите цифру: '))
                            if type_fire == 1:
                                    warHelicopter.fire_machine_gun()
                                    break
                            elif type_fire == 2:
                                warHelicopter.stop_fire_machine_gun()
                                break
                            elif type_fire == 3:
                                warHelicopter.rocket_fire()
                                break
                            elif type_fire == 4:
                                warHelicopter.stop_rocket_fire()
                                break
                            else:
                                print('Нет таких вариантов')
                                break

                        elif type_Helicopter == 3:
                            passangerHelicopter = PassengerHelicopter(int(input('Цена билета (бел.руб): ')), 'brand',
                                                                      'country_of_origin', 'engine_type', 'weight', 'color')

                            type_culc_flight_price = int(input(' Чтобы рассчитать время вашего полёта введите цифру 1\n'
                                                               'Чтобы завершить программу введите цифру 2\n'
                                                               'Введите цифру: '))
                            if type_culc_flight_price == 1:
                                passangerHelicopter.calculation_flight_price()
                                break
                            elif type_culc_flight_price == 2:
                                break
                            else:
                                print('Нет таких вариантов')
                                break
            helicopter()
    elif type_main == 4:
        waterTransport = WaterTransport()





    break

from random import randint


class Car:
    def __init__(self, color, name, is_police=None):
        self.speed = 0
        self.color = color
        self._name = name
        self._is_police = is_police if is_police is not None else False

    def go(self, speed=None):
        if speed is None:
            self.speed = randint(1, 100)
        else:
            self.speed = speed
        print(f'Машина поехала со скоростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Машина едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60} км/ч')
        else:
            print(f'Машина едет со скоростью {self.speed} км/ч')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40} км/ч')
        else:
            print(f'Машина едет со скоростью {self.speed} км/ч')


class SportCar(Car):
    def go(self, speed=None):
        if speed is None:
            self.speed = randint(1, 180)
        else:
            self.speed = speed
        print(f'Машина поехала со скоростью {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)

    def flashers(self):
        print('Мигалки включены')


car = Car('Белая', 'Mazda')
car.show_speed()
car.go()
car.turn('налево')
car.stop()
car.show_speed()
print(car._name)

town_car = TownCar('Черная', 'Лада')
town_car.go()
town_car.show_speed()

work_car = WorkCar('Синяя', 'Nissan')
work_car.go(56)
work_car.show_speed()

sport_car = SportCar('Зеленая', 'Lamborgini')
sport_car.go()
sport_car.show_speed()
sport_car.stop()
sport_car.show_speed()

police_car = PoliceCar('Синяя', 'Лада')
police_car.flashers()
police_car.go()
police_car.show_speed()

"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')
        pass


class TownCar(Car):

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')
        if self.speed > 60:
            print('Превышение скорости для TownCar')
        pass


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')
        if self.speed > 40:
            print('Превышение скорости для WorkCar')


class Police(Car):
    pass


tc1 = TownCar()
tc1.speed = 70
tc1.color = 'Red'
tc1.name = 'Ford focus'
tc1.is_police = False

tc1.go()
tc1.turn('направо')
tc1.show_speed()

p1 = Police()
p1.speed = 90
p1.color = 'White'
p1.name = 'Porsche 911'
p1.is_police = True

p1.go()
p1.show_speed()
p1.turn('налево')

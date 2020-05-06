from random import choice


class Homo:
    __population = 0

    def __init__(self, eye_color):
        self.age = 0
        self.sex = choice(('m', 'f'))
        self.eye_color = eye_color
        Homo.__population += 1


homo1 = Homo(eye_color='Red')
homo2 = Homo(eye_color='Green')

print(1)

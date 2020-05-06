"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'award': 0}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        wage = int(self._income['wage'])
        award = int(self._income['award'])
        return wage + award


user_1 = Position()
user_1.name = 'Gordon'
user_1.surname = 'Freeman'
user_1.position = 'Freelancer'
user_1._income = {'wage': 250000, 'award': 50000}

print(f'{user_1.get_full_name()} - {user_1.position} (total income: {user_1.get_total_income()})')

print(user_1.get_full_name())
print(user_1.get_total_income())

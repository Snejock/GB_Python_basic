# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import cycle, count
from time import sleep

start = 112
for i in count(start):
    print(i)
    sleep(0.5)

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
for i in cycle(my_list):
    print(i)
    sleep(0.5)

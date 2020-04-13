# var = 123
# a = (var % 10 - 0) // 1 # a = 3 - 0 // 1 = 3
# b = (var % 100 - a) // 10 # a = 23 - 3 // 10 = 2
# c = (var % 1000 - b) // 100 # a  = 123 - 23 // 100 = 1

var = int(input('Введите целое положительное число: \n'))  # Add checking type var is digit and don't start at '0'

i = 1
digit_depth = 1
remainder = 0
max_digit = 0
while i >= 1:
    digit = (var % (digit_depth * 10) - remainder) // digit_depth
    digit_depth = digit_depth * 10
    remainder = var % digit_depth
    i = var // digit_depth
    if digit > max_digit:
        max_digit = digit
print(f'Максимальное число: {max_digit}')



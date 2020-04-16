var = int(input('Введите число n:\n'))  # Add checking type var is digit
var_sum = var + (var + var*10) + (var + var * 10 + var * 100)

print(var_sum)

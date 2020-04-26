# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.


def my_func(arg_1: int, arg_2: int, arg_3: int) -> int:
    local_list = [arg_1, arg_2, arg_3]
    local_list.sort()
    local_list.pop(0)
    return sum(local_list)


a = int(input('Введите первый аргумент: \n'))
b = int(input('Введите второй аргумент: \n'))
c = int(input('Введите третий аргумент: \n'))

print(my_func(a, b, c))

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def sum_func(s: str):
    """
    Функция проверки на спецсимвол и представление строки в виде списка int значений
    """
    num_list = []
    global exit_flag
    exit_flag = False
    for itm in s:
        if itm == 'x':
            exit_flag = True
            break
        itm = int(itm)
        num_list.append(itm)
    return num_list


summary = 0
while True:
    user_str = input('Введите строку чисел, разделенных пробелом: \n')
    user_str = user_str.split(' ')
    summary = summary + sum(sum_func(user_str))

    print(f'Сумма равна: {summary}')
    if exit_flag is True:
        print('Завершение программы')
        break

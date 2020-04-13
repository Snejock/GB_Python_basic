profit = input('Введите выручку компании (в руб.): \n')
costs = input('Введите издержки компании (в руб.: \n')

fin_res = int(profit) - int(costs)

if fin_res > 0:
    print('Ваша компания прибыльна!')
    profitability = fin_res / int(profit)
    print(f'Рентабильность составляет: {profitability}')
    workers_number = input('Введите численность компании:\n')
    norm_profitability = fin_res / int(workers_number)
    print(f'Норма прибыли на одного сотрудника: {norm_profitability}')
elif fin_res < 0:
    print('Ваша компания убыточна!')
else:
    print('Ваша компания находится в состоянии самоокупаемости.')


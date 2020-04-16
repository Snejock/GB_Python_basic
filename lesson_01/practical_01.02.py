time_sec = input('Введите время в секундах:')

hours = int(time_sec) // 3600
time_sec = int(time_sec) - hours * 3600
minutes = int(time_sec) // 60
seconds = int(time_sec) % 60


print(f'Время в формате чч:мм:сс: {hours:>02}:{minutes:>02}:{seconds:>02}')

name = input('Введите имя пользователя\n')
while True:
    age = input('Введите ваш возраст\n')
    if age.isdigit():
        age = int(age)
        break
    else:
        print('Ошибка ввода данных. Введите только число.')


print(type(age))
print('Добрый день', name + '!')
if age >= 18:
    print('Доступ разрешен к фильмам 18+')
elif age >= 12:
    print('Доступ разрен к фильмам 12+')
else:
    print('Доступ разрешен к фильмам')


# i = 0
# while i < 10:
#     print(i)
#     if i == 4:
#         break
#     # if i == 3:
#     #     i += 2
#     #     continue
#     i += 1
# else:
#     print('WHILE ELSE')
# print('#' * 10)

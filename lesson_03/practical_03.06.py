# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(s: str):
    return s.title()


user_str = input('Введите несколько слов, разделенных пробелами: \n')
user_str = user_str.split(' ')

title_str = ''
for itm in user_str:
    title_str = (f'{title_str} {int_func(itm) }')


print(title_str.strip())

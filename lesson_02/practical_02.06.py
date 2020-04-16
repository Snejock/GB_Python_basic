# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
main_structure = []
products_list = []
i = 1
while i <= 2:
    products_list = [i, {'название': input('Введите название продукта: \n'),
                         'цена': int(input('Введите цену продукта: \n')),
                         'количество': int(input('Введите количество продуктов: \n')),
                         'ед.': input('Введите размерность количества: \n')}]
    products_tuple = tuple(products_list)
    main_structure.append(products_tuple)
    i += 1

print(main_structure)

name_set = set()
price_set = set()
stock_set = set()
measure_set = set()

itm = 0
for itm in main_structure:
    name_set.add(itm[1]['название'])
    price_set.add(itm[1]['цена'])
    stock_set.add(itm[1]['количество'])
    measure_set.add(itm[1]['ед.'])

name_dict = {'название': list(name_set)}
price_dict = {'цена': list(price_set)}
stock_dict = {'количество': list(stock_set)}
measure_dict = {'ед.': list(measure_set)}

analytic_structure = dict()
analytic_structure.update(name_dict)
analytic_structure.update(price_dict)
analytic_structure.update(stock_dict)
analytic_structure.update(measure_dict)

print(analytic_structure)
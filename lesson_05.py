import requests

url = 'https://geekbrains.ru/'

response = requests.get(url)
# file = open('test.html', 'w', encoding='UTF-8')
# try:
#     file.write(response.text)
# except IOError:
#     pass
# finally:
#     file.close()

with open('test.html', 'r', encoding='UTF-8') as file:
#    for line in file:
#        print(line, end='')
    print(file.read())

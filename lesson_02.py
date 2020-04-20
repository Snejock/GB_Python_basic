a = 'Hello world!'
b = ['Next', 1, 2, 3, 4, 5, 6]

for itm in b[:]:
    b.append(itm * 2)

print(b)

# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

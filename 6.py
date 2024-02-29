weight=int(input('Введите вес в фунтах: '))
ft=int(input('Введите рост в дюймах: '))
print(round((weight/(ft**2))*703, 2))
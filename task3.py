# По заданному номеру дня недели вывести его название

def find_day (number):
    if number == 1:
        return ('monday')
    elif number == 2:
        return ('tuesday')
    elif number == 3:
        return ('wednesday')
    elif number == 4:
        return ('thursday')
    elif number == 5:
        return ('friday')
    elif number == 6:
        return ('saturday')
    elif number == 7:
        return ('sunday')
    else:
        return ('does not exist')

print('Введите номер дня: ')
n = int(input())
print(find_day(n))
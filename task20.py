# Задать номер четверти, показать диапазоны для возможных координат

def quarter (q):
    d = ''
    if q == 1:
        d = 'x > 0, y > 0'
    elif q == 2:
        d = 'x < 0, y > 0'
    elif q == 3:
        d = 'x < 0, y < 0'
    elif q == 4:
        d = 'x > 0, y < 0'
    else:
        d = 'четверть не существует'
    return(d)

print('Введите номер четверти: ')
q = int(input())
print(quarter(q))
# Даны два числа. Показать большее и меньшее число

def find_maxmin (first, second):
    if first > second:
        return (f'{first} - max, {second} - min')
    else:
        return (f'{second} - max, {first} - min')

print('Введите первое число: ')
first = int(input())
print('Введите второе число: ')
second = int(input())
print(find_maxmin(first, second))
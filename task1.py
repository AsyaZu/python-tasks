# По двум заданным числам проверять является ли первое квадратом второго

def square (first, second):
    return (second ** 2 == first)

print('Введите первое число: ')
first = int(input())
print('Введите второе число: ')
second = int(input())
print(square(first, second))
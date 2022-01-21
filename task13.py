# Выяснить, кратно ли число заданному, если нет, вывести остаток

def multiplicity (num1, num2):
    return(num1 % num2 == 0)

print('Введите первое число: ')
num1 = int(input())
print('Введите второе число: ')
num2 = int(input())
print(multiplicity(num1, num2))

if multiplicity(num1, num2) == 0:
    print(f'Остаток от деления: {num1 % num2}')
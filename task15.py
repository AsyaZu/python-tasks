# Дано число. Проверить кратно ли оно 7 и 23
def check (n):
    return(n % 7 == 0 and n % 23 == 0)

print('Введите число: ')
n = int(input())
print(check(n))
# Подсчитать сумму цифр в числе

def sum (num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = (num - num % 10) // 10
    return sum
print(sum(123))
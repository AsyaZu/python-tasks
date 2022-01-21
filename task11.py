# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

import random
n = random.randint(10, 99)
print(n)

def find_max (n):
    max = n // 10
    if n % 10 > n // 10:
        max = n % 10
    return(max)
    
print(find_max(n))
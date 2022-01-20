# Найти максимальное из трех чисел

def find_max (a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    if a == b == c:
        max = 'the numbers are equal'
    return (max)

print(find_max(21, 2, 12))
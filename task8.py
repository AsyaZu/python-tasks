# Показать четные числа от 1 до N

def show_even_numbers (n):
    list = []
    for i in range (1, n + 1):
        if i % 2 == 0:
            list.append(i)
    return (list)
print(show_even_numbers(10))
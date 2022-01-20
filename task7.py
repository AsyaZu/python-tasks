# числа от -N до N

def show_numbers(n):
    list = []
    for i in range (-n, n + 1):
        list.append(i)
    return (list)
print(show_numbers(5))    
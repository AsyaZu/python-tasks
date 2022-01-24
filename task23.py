# Показать таблицу квадратов чисел от 1 до N 

def square (n):
    list = []
    for i in range(1, n + 1):   
       list.append(i**2)
    return list
print(square(5))
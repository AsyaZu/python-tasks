# Задать массив из 12 элементов, заполненных числами из [-10,10]. Найти сумму положительных/отрицательных элементов массива

import random
def array (list):
    for i in range(0, 12):
        i = random.randint(-10, 10)
        list.append(i)
    return list

def sum (list):
    sum_pl = 0
    sum_mn = 0
    for i in list:
        if i >= 0:
            sum_pl += i
        else:
            sum_mn += i
    return(f'Сумма положительных эллементов {sum_pl}, сумма отрицательных эллементов {sum_mn}')

list = []
print(array(list))
print(sum(list))


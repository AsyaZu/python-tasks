# Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран 

import random

def array (list):
    for i in range (0, 8):
        i = random.randint(0, 1)
        list.append(i)
    return list
list = []    
print(array(list))
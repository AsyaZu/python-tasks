# Задать массив из 8 элементов и вывести их на экран 
import random

def array (list):
    for i in range (0, 8):
        i = random.randint(-10, 10)
        list.append(i)
    return list
list = []    
print(array(list))
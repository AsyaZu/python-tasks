# Определить, присутствует ли в заданном массиве, некоторое число 
import random
def array (list):
    for i in range(0, 5):
        i = random.randint(0, 10)
        list.append(i)
    return list

def find_el (list, num):
    return (num in list)

list = []
print(array(list))
print(find_el(list, 3))
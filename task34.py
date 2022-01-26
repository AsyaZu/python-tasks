# Написать программу замену элементов массива на противоположные
import random
def array (list):
    for i in range(0, 5):
        i = random.randint(-10, 10)
        list.append(i)
    return list

def change_array (list):
    for i in range(0, 5):
        list[i] = -1*list[i]
    return list

list = []
print(array(list))
print(change_array(list))
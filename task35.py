# Определить, присутствует ли в заданном массиве, некоторое число 
import random
def array (list):
    for i in range(0, 5):
        i = random.randint(0, 5)
        list.append(i)
    return list

def find_el (list, num):
    answer = 'false'
    for i in list:
        if i == num:
            answer = 'true '
    return answer

list = []
print(array(list))
print(find_el(list, 3))
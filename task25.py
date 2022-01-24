#  Найти сумму чисел от 1 до А

def sum (a):
    answer = 0
    for i in range(1, a + 1):
        answer += i
    return answer
print(sum(4))
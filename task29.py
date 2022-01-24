# Написать программу вычисления произведения чисел от 1 до N

def fact (n):
    if n == 1:
        answer = 1
    else:
        answer = n * fact(n - 1)
    return answer
print(fact(3))

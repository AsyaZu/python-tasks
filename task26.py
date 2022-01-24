# Возведите число А в натуральную степень B используя цикл

def degree (a, b):
    answer = 1
    for i in range(1, b + 1):
        answer *= a
    return answer
print(degree(2, 3))
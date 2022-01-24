# Найти кубы чисел от 1 до N

def cube (n):
    answer = ''
    for i in range(1, n + 1):
        answer += f'{i}**3={i**3}\n'
    return answer
print(cube(5))
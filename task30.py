# Показать кубы чисел, заканчивающихся на четную цифру

def cube (n):
    answer = ''
    for i in range(1, n + 1):
        if (i**3) % 2 == 0:
            answer += f'{i**3} '
    return answer

print(cube(7))
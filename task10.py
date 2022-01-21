# Показать вторую цифру трёхзначного числа

def second_figure (n):
    return (n % 100 // 10)
print(second_figure(123))
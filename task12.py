# Удалить вторую цифру трёхзначного числа

def delete_figure (n):
    last = n % 10
    first = n // 10
    final = first - first % 10 + last
    return(final)
print(delete_figure(531))
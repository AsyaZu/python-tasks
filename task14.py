# Найти третью цифру числа или сообщить, что её нет (с конца)

def find_figure (n):
    if n // 100 == 0 and n % 100 > 0:
        number = 'цифры нет'
    else:
        number = n % 1000 // 100
    return(number)
print(find_figure(69583))



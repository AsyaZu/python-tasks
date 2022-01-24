# Определить количество цифр в числе

def count (num):
    count = 0
    while num > 0:
        num = num // 10
        count = count + 1
    return count
print(count(2789))
    
    
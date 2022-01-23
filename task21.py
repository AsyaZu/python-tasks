# Программа проверяет пятизначное число на палиндромом

def palindrome (num):
    fifth = num % 10
    fourth = num % 100 // 10
    third = num % 1000 // 100
    second = num // 1000 % 10
    first = num // 10000
    return(fifth == first and fourth == second)
print(palindrome(83238))


# По двум заданным числам проверять является ли одно квадратом другого

def square (num1, num2):
    return(num1**2 == num2 or num2**2 == num1) 
    
print('Введите первое число: ')
num1 = int(input())
print('Введите второе число: ')
num2 = int(input())
print(square(num1, num2))
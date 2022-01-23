# Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

def quarter (x, y):
    q = ''
    if x > 0 and y > 0:
        q = '1'
    elif x < 0 and y > 0:
        q = '2'
    elif x < 0 and y < 0:
        q = '3'
    else:
        q = '4'
    return(q)
        
print('x: ')
x = int(input())
print('y: ')
y = int(input())
print(quarter(x, y))
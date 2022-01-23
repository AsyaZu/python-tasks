# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

def check (X, Y, Z):
    return(not (X or Y or Z) == (not X and not Y and not Z))

for X in range (0, 2):
    for Y in range (0, 2):
        for Z in range (0, 2):
            print(check(X, Y, Z))
def horner(koefficient, x):
    result = koefficient[0]
    for i in range(1, len(koefficient)):
        result = result * x + koefficient[i]
    return result
koefficient = [2, -6, 2, -1] 
x = 3
print(horner(koefficient, x)) 
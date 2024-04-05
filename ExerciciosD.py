numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10 ,11 ,12 ,13 ,14, 15]
numeros_elevedos = []

for numero in numeros:
    quadrado = numero **2
    numeros_elevedos.append(quadrado)

for a, b in zip(numeros, numeros_elevedos):
    print(f'{a} elevedo é {b}')

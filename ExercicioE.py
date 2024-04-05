numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10 ,11 ,12 ,13 ,14, 15]
numeros_fatorial = []

contador = 1
fatorial = 1
for numero in numeros:
    fatorial = fatorial * contador
    contador += 1
    numeros_fatorial.append(fatorial)

for a, b in zip(numeros, numeros_fatorial):
    print(f'{a} O fatorial do numero é {b}')
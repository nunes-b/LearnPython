matriz = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
print(matriz)
print(matriz[0][0], matriz[1][0], matriz[2][0], matriz[3][0])
print(matriz[0][1], matriz[1][1], matriz[2][1], matriz[3][1])
print(matriz[0][2], matriz[1][2], matriz[2][2], matriz[3][2])

print("*****************************************************")
lista = ["p", "y", "t", "h", "o", "n"]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

print("*****************************************************")
# Iterando listas ->
carros = ["BMW", "Mercedes", "Audi", "Jeep"]
# for carro in carros:
#     print(carro)
print("*****************************************************")
for index, carro in enumerate(carros):
    print(f"{index}: {carro}")
print("*****************************************************")
print(carros[3])
print("*****************************************************")


numeros = [1, 30, 20, 4, 5, 6, 12, 20, 6, 3, 2]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
print("*****************************************************")

numeros = [2, 4, 6, 8, 10]
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)
print("*****************************************************")

numeros2 = [1, 2, 3, 4, 5, 6]
quadrado2 = [numero ** 2 for numero in numeros2]

print(quadrado2)
print("*****************************************************")

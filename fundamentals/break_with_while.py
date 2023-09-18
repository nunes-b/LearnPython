# exemplo com while
while True:
    numero = int(input("Informe um numero:"))
    if numero == 10:
        break

print(numero)

# exemplo com for
for numeros in range(100):
    if numeros == 12:
        break

print(numeros, end="")

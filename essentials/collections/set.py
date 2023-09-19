# Set elimina registros duplicados por ex:
print(set([1, 1, 2, 3, 4, 5, 6, 1]))

print(set("Abacaxi"))

print(set(("Palio", "Gol", "Celta", "Palio", "Gol",)))

# Não se pode confiar no set para odernar.

carros = {"Carrinho", "Carrão", "Carreta", "Carreta", "Carreta"}
print(carros)

carros = list(carros)
print(carros[0])

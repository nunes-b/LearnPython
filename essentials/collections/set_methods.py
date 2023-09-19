# {}.union --> conjunto matematico para a união
conjunto_a = {1, 2}
conjunto_b = {3, 4}
# print(conjunto_a.union(conjunto_b))

# {}.intersection --> a parte que eles estão se tocando se repete para ambos
conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}
# print(conjunto_c.intersection(conjunto_d))

# {}.difference --> metodo que tira a diferença dos conjuntos
conjunto_z = {1, 2, 3}
conjunto_y = {3, 4, 5}

print(conjunto_y.difference(conjunto_z))
print(conjunto_z.difference(conjunto_y))

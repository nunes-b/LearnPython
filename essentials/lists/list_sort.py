# [].sort -> Ordena a lista
linguagens = ["Python", "JavaScript", "C", "Java", "C#", ".NET"]
print(linguagens)

linguagens.sort()
print(linguagens)

# Reverte
linguagens.sort(reverse=True)
print(linguagens)

# -> Do menor pro maior ["...index"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)

# -> Do maior pro menor ["... index"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

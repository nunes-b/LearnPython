texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(f"Vogais dentro de {texto} é:", letra, '\n', end='\0')
else:
    print("Fim da aplicação.")

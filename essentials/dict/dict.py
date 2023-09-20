# Dicionario de dados
pessoa = dict(nome="Rômulo", idade=24)
pessoa["telefone"] = "219994-9993"
# print(pessoa)

pessoa["nome"] = "Jesus"
# print(pessoa)


contatos = {
    "romulo@geoflow.com.br": {"nome": "Rômulo", "telefone": "21-9999-9999"},
    "alano@geoflow.com.br": {"nome": "Alano", "telefone": "21-9999-9999"}
}

nome = contatos["alano@geoflow.com.br"]["nome"]
# print(nome)

for chave, valor in contatos.items():
    print(chave, contatos[chave])

contatos = {
    "romulo@geoflow.com.br": {"nome": "Rômulo", "telefone": "21-9999-9999"},
    "alano@geoflow.com.br": {"nome": "Alano", "telefone": "21-9999-9999"}
}
contatos2 = contatos.copy()
print(contatos)
print(f"Contatos 2: {contatos2}\n")
print("===============================================================================")
contatos.clear()
print(contatos)
print("===============================================================================")

# {}.fromkeys -> Ele cria chaves pro seu dict
print("Exemplo de FromKeys.")
print(dict.fromkeys(["Nome", "Telefone"]))
print(dict.fromkeys(["Nome", "Telefone"], "vazio"))
print("===============================================================================")

# {}.get -> Ele busca informações no dict através de parametros.
users = {
    "rnunes-b": {"nome": "Rômulo", "telefone": "(21)9994-9090"},
    "nunes-br": {"nome": "Remulo", "telefone": "(21)9993-9393"}
}

result = users.get("rnunes-b", {})
print(result)

# {}.items -> Retorna items do dict

contatos = {
    "rnunes-b": {"Nome": "Rômulo", "Telefone": "+55 (021)1234-6789"}
}
result_items = contatos.items()
print(result_items)
result2_items = contatos.keys()
print(result2_items)

# {}.setdefault -> Seta um valor como default se ele não encontrar um objeto com valor
contato = {
    "nome": "romulo", "telefono": "+555 123-345-123"
}
contato.setdefault("lá idad", 13)
print(contato)

# {}.update -> ele atualiza e mostra os campos dentro do dict.
employer = {
    "dev": {"name": "Rômulo", "role": "jr", "value": "A", "salary": "$7000.00c"}
}
employer.update({"dev": {"name": "Remule"}})
print(employer)
employer.update({"dev": {"bens": "mercedes-rich-benz"}})
print(employer)

def exibir_mensagem():
    print("Olá, mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_dados_do_usuario():
    nome = input("Qual seu nome? ")
    sobrenome = input("Qual seu sobrenome? ")
    idade = input("Qual a sua idade? ")
    print(f"Olá {nome} {sobrenome}, seja muito bem vindo! é muito bom saber que a sua idade é {idade}.")


def exibir_mensagem_3(nome="none"):
    print(f"Seja bem vindo {nome}!")


# exibir_dados_do_usuario()
# exibir_mensagem()
# exibir_mensagem_2(nome="Filipino")
# exibir_mensagem_3()
# exibir_mensagem_3(nome="Jubileu")

def calcular_total(numeros):
    return sum(numeros)


# calcular_total([10, 2, 10])


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor


# print(retorna_antecessor_e_sucessor(10))


def salvar_modelo_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_modelo_carro("Fiat", "Palio", 1999, "ABC-123")


def make_a_car():
    print("Olá, tudo bem? siga respondendo algumas perguntas para adicionarmos seu veiculo em nossos registros.")
    marca = input("Qual a montadora do veiculo? ")
    modelo = input("Qual é o modelo do veiculo? ")
    ano = input("Foi fabricado em que ano? ")
    placa = input(
        "Qual o final da placa do seu veiculo? apenas os dois ultimos numeros: ")
    print(
        f"Perfeito! o Seu veiculo pertenceu a montadora {marca} é do modelo {modelo} e foi fabricado no ano de {ano}, seu veiculo tem o final de placa com os numeros: {placa}.")


# make_a_car()

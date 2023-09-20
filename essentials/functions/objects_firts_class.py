def somar(a, b):
    return a + b


def dividir(a, b):
    return a / b


def subtrair(a, b):
    return a - b


def mostrar_resultado(a, b, funcao):
    resultado = funcao(a, b)
    if funcao == somar:
        print(f"O resultado da operação {a} + {b} = {resultado}")
    if funcao == subtrair:
        print(f"O resultado da operação {a} - {b} = {resultado}")
    if funcao == dividir:
        print(f"O resultado da operação {a} / {b} = {resultado}")


mostrar_resultado(10, 5, somar)

def sacar(valor):
    saldo = 400

    if saldo >= valor:
        print(f"Seu saldo no dia é de R$ {saldo}")
        print(f"Foram sacados R$ {valor} reais.")
        subtracao = saldo - valor
        print(f"Seu novo saldo é de: R$ {subtracao}")


print("Obrigado por utilizar o nosso sistema, estamos com problemas, volte em breve.")


sacar(1500)

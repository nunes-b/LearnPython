conta_normal = False
conta_universitaria = False
saldo = 1000
saldo_universitario = 500
saque = 100
cheque_especial = 500

if conta_normal:
    if saldo >= saque:
        print(f"Saque realizado com sucesso. R${saque}.")
    elif saque <= (saldo + cheque_especial):
        subtracao = (saldo + cheque_especial) - saque
        print(f"Seu saldo de cheque especial: R${cheque_especial}.")
        print(
            f"Saque de R${saque}. realizado com o uso do cheque especial seu valor atualizado com uso do cheque. {subtracao}.")
    else:
        print(f"Saldo insuficiente.")

elif conta_universitaria:
    if saldo_universitario >= saque:
        print(f"Saque realizado com sucesso, no valor de R${saque}.")
    else:
        print(
            f"Saldo insuficiente, verifique o valor digitado, você detem em conta R${saldo_universitario}")
else:
    print("ERROR! \n O nosso sistema não reconheceu sua conta, entre em contato com o seu gerente ou em nossos canais telefonicos: 4004-4003")

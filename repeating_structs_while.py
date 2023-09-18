opcao = -1

while opcao != 0:
    opcao = int(
        input("\n [1] Para Saque \n [2] Para Extrato \n [0] Para Sair \n Digite a sua opção: "))
    if opcao == 1:
        print("Saque realizado com sucesso.")
    elif opcao == 2:
        print("Seu extrato está sendo imprimido.")
else:
    print("Obrigado por utilizar de nossos serviços. Até logo =D")

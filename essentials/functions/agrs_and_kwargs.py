def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join(
        [f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}."
    print(mensagem)


exibir_poema("Sexta-feira 26 de agosto de 1999", "Zen of python!", "Beautiful is better than ugly.",
             author="Tim Peters", ano=1999)
# Chave valor é Kwargs.

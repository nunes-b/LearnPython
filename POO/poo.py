# Self é uma referencia para o objeto --> algo parecido com this.
class Bike:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

# Metodos para bike -> Metodos são coisas parecidas com funções
    def buzinar(self):
        print("Biiiiiiiiiiiiiii")

    def parar(self):
        print("Desacelerando...shhhhhh")
        print("Par ou a bicicleta")

    def correr(self):
        print("Acelerandooooo")
        print("Vruuuuuuuum")

    # def __str__(self):
    #     return f"Bicicleta de cor: {self.cor}, modelo: {self.modelo}, ano: {self.ano} e custa: {self.valor}"
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


caloi = Bike(cor="Preta", modelo="Caloi", ano=2022, valor="R$600")
print(caloi)

caloi.buzinar()
caloi.correr()
caloi.parar()

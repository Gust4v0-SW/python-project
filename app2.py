class Estado:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def inserir(self, estado):
        posicao = self.funcaoHash(estado.sigla)
        estado.proximo = self.tabela[posicao]
        self.tabela[posicao] = estado

    def funcaoHash(self, sigla):
        if sigla == "DF":
            return 7
        else:
            valor = ord(sigla[0]) + ord(sigla[1])
            posicao = valor % 10
            return posicao

    def imprimir(self):
        for i in range (10):
            atual = self.tabela[i]
            if atual == None:
                print("None")
            else:
                print("Posição", i, end=": ")
                while atual != None:
                    print(atual.sigla, end=" -> ")
                    atual = atual.proximo
                print(atual)

    def imprimirTabelaInicial(self):
        for i in range(10):
            print(i, ":", self.tabela[i])

hash = TabelaHash()

print("##########################################")
print("Tabela inicial, sem dados:")
print("##########################################")
hash.imprimirTabelaInicial()

estados = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins")
]

for sigla, nome in estados:
    estado = Estado (sigla, nome)
    hash.inserir(estado)

print("##########################################")
print("Tabela com os 26 estados + o distrito:")
print("##########################################")
hash.imprimir()

estadoFicticio = Estado("GK", "Gustavo Rafael Karasek Ott")
hash.inserir(estadoFicticio)
print("##########################################")
print("Tabela com o estado fictício:")
print("##########################################")
hash.imprimir()

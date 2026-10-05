class senha:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class listaSenhas:
    def __init__(self):
        self.head = None
        self.contadorV = 1
        self.contadorA = 201

    def inserirSemPrioridade(self, senha):
        atual = self.head
        while atual.proximo != None:
             atual = atual.proximo
        atual.proximo = senha

    def inserirComPrioridade (self, senha):
        anterior = None
        atual = self.head
        while atual != None and atual.cor == "A":
            anterior = atual
            atual = atual.proximo

        if anterior == None:
            senha.proximo = atual
            self.head = senha
        else:
            senha.proximo = atual
            anterior.proximo = senha

    def inserir(self):
        cor = input("Digite a cor da senha (A/V): ").upper()
        if cor == "A":
             numero = self.contadorA
             self.contadorA = self.contadorA +1
        elif cor == "V":
            numero = self.contadorV
            self.contadorV = self.contadorV +1
        else:
            print("Você não digitou uma opção válida")
            return

        novaSenha = senha(numero, cor)
        if self.head == None:
            self.head = novaSenha
        else:
            if cor == "V":
                self.inserirSemPrioridade (novaSenha)
            elif cor == "A":
                self.inserirComPrioridade(novaSenha) 


    def imprimirListaEspera(self):
        atual = self.head
        while atual != None:
            print("[ ", atual.cor, atual.numero, " ]", end=" -> " )
            atual = atual.proximo
        print("")    

    def atenderPaciente(self):
        if self.head == None:
            print("Não ha pacientes na fila de espera")
        else:
            atual = self.head
            self.head = atual.proximo
            print("Chamando paciente: " + atual.cor, atual.numero)
op = 0
lista = listaSenhas()
while op !=4:
    print("###################################")
    print("###### TRIAGEM FILA DE ESPERA #####")
    print("###################################")
    print("Escolha uma opção:")
    print("")
    print("1 - Adicionar paciente a fila")
    print("2 - Mostrar pacientes na fila")
    print("3 - Chamar um paciente")
    print("4 - Sair")
    print("")
    op= int(input("Digite a opção >> "))

    if op == 1:
        lista.inserir()
    elif op ==2:
        lista.imprimirListaEspera()
    elif op == 3:
        lista.atenderPaciente()
    elif op ==4:
        break
    else:
        print("Você digitou uma opção inválida")    


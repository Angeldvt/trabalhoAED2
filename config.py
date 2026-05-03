#Inserir, Remover, Acessar, Exibir estrutura, Buscar informação, Acessar informação

class lista_linear:
    def __init__(self, n_max):
        self.tamanho = n_max
        #self.lista = [None] * self.tamanho

        self.lista = []
        self.lista.append(None)
        self.lista.append(None)
        self.lista.append(None)
        self.lista.append(None)
        self.lista.append(None)
        self.lista.append(None)
        self.lista.append(1)
        self.lista.append(2)
        self.lista.append(3)
        self.lista.append(4)
        
        self.inicio = 6
        self.fim = 9


    # Verifica se a lista está vazia
    def isVazia(self):
        if self.inicio == -1 and self.fim == -1:
            return True
        return False

    
    def getTamanho(self):
        if self.isVazia():
            return 0 # retorna vazia
        if self.fim >= self.inicio:
            return self.fim - self.inicio + 1 # retorna o tamanho para lista normal
        else:
            return self.tamanho - self.inicio + self.fim + 1 # retorna tamanho da lista circular
            #           10      -       9     +     8)   + 1     [L4,L5,L6,L7,L8,L9,L10,L1,L2,L3]


    def isCheia(self):
        return (self.fim == (self.inicio-1))


    def inserir(self, dado, posicao: int=None): # Se a posição nao receber nada, o item será adicionado ao fim da lista atual
        tamanho = self.getTamanho()
        print(f'tamanho: {tamanho}')
        
        if self.isCheia():  # bloqueia caso cheia
            print("Lista cheia. Não foi possível inserir.")
            return False
        
        if posicao == None:
            posicao = tamanho+1 # o item será colocado no final da lista


        if not (tamanho+1 >= posicao >= 0): # verifica se a posição desejada está entre (inicio-1) e (fim+1)
            print("\033[31m>>erro 1<<\033[m")
            return False


        if self.inicio == 0:    # casos apenas para quando a lista começa no indice 0
            if posicao == tamanho+1:    # caso ideal perfeito amém
                print("\033[31m>> . <<\033[m")
                print("\033[31m>> caso ideal <<\033[m")
                self.lista[posicao-1] = dado
            else:
                print("\033[31m>>  posicao menor q tamanho  <<\033[m")  # caso a posição desejada seja uma posição já ocupada
                #print(posicao-1, tamanho)
                empurra = True
                while empurra:  # loop para empurrar outros dados para posições ainda não ocupadas e permitir a inserção do dado na posição desejada
                    for i in range(0, tamanho+1):
                        if self.lista[i] == None:
                            #print(i, "-", self.lista[i])
                            self.lista[i] = self.lista[i-1]
                            self.lista[i-1] = None
                            #lista.exibir_estrutura()
                            if (posicao == i):
                                self.lista[i-1] = dado
                                empurra = False
        
        else:   # caso (self.inicio != 0), ou seja, caso o inicio da lista não seja no índice zero
            if self.inicio < self.fim:  # caso o inicio esteja antes do fim, ou seja, a lista ainda não é circular
                print(f'pos: {posicao} / self.inicio: {self.inicio} / pos+ini: {self.inicio+posicao}')
                posicao += self.inicio
                if posicao == tamanho+self.inicio+1:    # caso ideal perfeito amém
                    if (self.fim == self.tamanho-1):
                        self.lista[0] = dado
                        return True
                    print("\033[31m>> . <<\033[m")
                    print("\033[31m>> caso ideal <<\033[m")
                    self.lista[posicao-1] = dado
                
                else:
                    print("\033[31m>>  posicao menor q tamanho  <<\033[m")  # caso a posição desejada seja uma posição já ocupada
                    #print(posicao-1, tamanho)
                    fronteira = False
                    #print(f' posicao {posicao} / self.tamanho {self.tamanho}')
                    if self.inicio <= posicao <= (self.tamanho):
                        fronteira = True
                        print("\033[31m>>  FRONTEIRA  <<\033[m")
                        self.lista[0] = self.lista[self.tamanho-1]
                        self.lista[self.tamanho-1] = None
                        lista.exibir_estrutura()
                    empurra = True
                    cont = 0
                    while empurra and not fronteira:  # loop para empurrar outros dados para posições ainda não ocupadas e permitir a inserção do dado na posição desejada
                        for i in range(self.inicio, tamanho+self.inicio+1):
                            if self.lista[i] == None:
                                #print(i, "-", self.lista[i])
                                self.lista[i] = self.lista[i-1]
                                self.lista[i-1] = None
                                #lista.exibir_estrutura()
                                if (posicao == i):
                                    self.lista[i-1] = dado
                                    empurra = False
                    while empurra and fronteira:
                        for i in range(self.inicio, tamanho+self.inicio):
                            print(">>>>", i, self.lista[i])
                            if self.lista[i] == None:
                                if (posicao-1 == i):
                                    self.lista[i] = dado
                                    empurra = False
                                #print(i, "-", self.lista[i])
                                else:
                                    self.lista[i] = self.lista[i-1]
                                    self.lista[i-1] = None
                                    #lista.exibir_estrutura()
                                print("teste >>> ", posicao, self.inicio, i, tamanho)
                                #if (posicao-1 == i):
                                #    self.lista[i] = dado
                                #    empurra = False

        if posicao >= (self.tamanho/2):
            pass



    def remover(self):
        pass
    def acessar(self):
        pass
    def exibir_estrutura(self):
        print("\n-- Lista:\n[", end="")
        for i in range(0, len(self.lista)):
            if self.lista[i]:  # --> só vai printar dados que não forem "None"
                if i < len(self.lista)-1:
                    print(f"{self.lista[i]}", end=", ")
                else:
                    print(f"{self.lista[i]}", end="]\n--\n")

    def buscar_info(self):
        pass
    def acessar_info(self):
        pass


# teste <<<
print()
lista = lista_linear(10)
#print(lista.isVazia())
#print(lista.getTamanho())

#print(lista.isCheia())

#lista.exibir_estrutura()
lista.exibir_estrutura()
print()

lista.inserir(99, 4)

lista.exibir_estrutura()
#Inserir, Remover, Acessar, Exibir estrutura, Buscar informação, Acessar informação
class Dado_da_Lista:
    def __init__(self, nodo, indice=-1, dado=None, anterior=None, proximo=None):
        self.dado_anterior = anterior
        self.dado_proximo = proximo
        self.dado = dado
        self.nodo = nodo
        self.indice = indice
    def alteraProximo(self, proximo):
        self.dado_proximo = proximo
    def alteraAnterior(self, anterior):
        self.dado_anterior = anterior
    def alteraNodo(self, n):
        self.nodo += n
    def alteraIndice(self, n):
        self.indice += n
    def getProximo(self):
        return self.dado_proximo
    
    def getAnterior(self):
        return self.dado_anterior

    def exibirSe(self):
        print(f'[ dado: {self.dado} / nodo: {self.nodo} / indice: {self.indice}', end=' / ')

        if self.dado_anterior != None:
            print(f'anterior: {self.dado_anterior.dado}', end=' / ')
        
        if self.dado_proximo != None:
            print(f'/ proximo: {self.dado_proximo.dado}', end=' ')
        print(']')

class Lista_circular:
    def __init__(self, n_max):
        self.maximo = n_max

        
        self.lista = [None] * self.maximo
        for i in range(0, self.maximo):
            self.lista[i] = Dado_da_Lista(nodo=-1, indice=i)
        
        for i in range(0, self.maximo): # apontando os anteriores
            if i == 0:
                self.lista[i].alteraAnterior(self.lista[self.maximo-1])
            else:
                self.lista[i].alteraAnterior(self.lista[i-1])

        for i in range(0, self.maximo): # apontando os próximos
            if i == self.maximo-1:
                self.lista[i].alteraProximo(self.lista[0])
            else:
                self.lista[i].alteraProximo(self.lista[i+1])
        
        self.inicio = -1
        self.fim = -1


    def getDadoFromNodo(self, n_nodo):
        for i in self.lista:
            print(f'i.nodo: {i.nodo} // n_nodo: {n_nodo}')
            if i.nodo == n_nodo:
                return i
        
        # caso ele nao ache a partir do Nodo:
        for i in self.lista:
            print(f'i.nodo: {i.nodo} // n_nodo: {n_nodo}')
            if i.nodo == n_nodo-1:
                return i

    # Verifica se a lista está vazia
    def montaLista(self):
        nova_lista = [None] * self.maximo
        for i in range(0, self.maximo):
            for j in self.lista:
                if j.indice == i:
                    nova_lista[i] = j
                    break
        
        self.lista = nova_lista[:]
            
            #nova_lista[i] = item
    def isVazia(self):
        if type(self.inicio) == int:
            if self.inicio == -1 and self.fim == -1:
                return True
        return False

    
    def getTamanho(self):
        if self.isVazia():
            return 0 # retorna vazia
        if type(self.inicio) == int:
            if self.fim >= self.inicio:
                return self.fim - self.inicio + 1 # retorna o tamanho para lista normal
            else:
                return self.maximo - self.inicio + self.fim + 1 # retorna tamanho da lista circular
                #           10      -       9     +     8)   + 1     [L4,L5,L6,L7,L8,L9,L10,L1,L2,L3]
        else:
            if self.fim.nodo >= self.inicio.nodo:
                return self.fim.nodo - self.inicio.nodo + 1 # retorna o tamanho para lista normal
            else:
                return self.maximo - self.inicio.nodo + self.fim.nodo + 1 # retorna tamanho da lista circular
                #           10      -       9     +     8)   + 1     [L4,L5,L6,L7,L8,L9,L10,L1,L2,L3]

    def isCheia(self):
        if type(self.inicio) == int:
            return (self.fim == (self.inicio-1))
        else:
            return ((self.fim.nodo == (self.inicio.nodo-1))) or (self.inicio.nodo == 0 and self.fim.nodo == self.maximo-1)

    def mostrar_dados(self):
        for i in self.lista:
                i.exibirSe()
    def inserir(self, dado, posicao: int=None):
        if self.isCheia():
            print('>>Lista cheia')
            return False
        
        if self.isVazia():
            if posicao == None:
                posicao = 0
            #else:
                #posicao -= 1
            #
            self.lista[posicao] = Dado_da_Lista(nodo=0, indice=posicao, dado=dado, anterior=None, proximo=None)
            self.lista[posicao].alteraAnterior(self.lista[posicao])
            self.lista[posicao].alteraProximo(self.lista[posicao])
            #
            self.inicio = self.lista[posicao]
            self.fim = self.lista[posicao]


            ''' funcao pra alterar o nodo dos None's - nao precisa mais...
            n_nodo = 2
            proximo_nodo = self.lista[posicao].getProximo()
            while proximo_nodo.nodo != 0:
                proximo_nodo.alteraNodo(n_nodo)
                proximo_nodo = proximo_nodo.getProximo()
                n_nodo += 1
                #print(proximo_nodo.nodo)
            '''
            
            return True
        
        else:   # caso nao esteja vazia--> aqui a posição será o nodo desejado
            if posicao == None:
                posicao = self.fim.nodo+1   # escolhe a posicao padrao fim+1
            #print(f'pos: {posicao} / ini.nodo+1: {self.fim.nodo+1}')

            if posicao == self.fim.nodo+1:  # caso a posicao desejada seja fim+1
                if self.fim.indice < (self.maximo-1):   # testa se o fim+1 está dentro dos limites
                    if self.inicio.indice <= self.fim.indice:   # testa se o inicio está antes do fim
                        temp_dado = Dado_da_Lista(nodo=posicao, indice=self.inicio.indice+posicao, dado=dado, anterior=self.fim, proximo=self.inicio)   # cria um obj temporario
                        
                        self.fim.alteraProximo(temp_dado)   # faz o antigo fim apontar para o novo fim
                        self.inicio.alteraAnterior(temp_dado)   # faz o inicio apontar para o novo fim
                        self.lista[self.fim.indice+1] = temp_dado   # posicao da lista vira o temp_dado (insere o dado)
                        self.fim = self.lista[self.fim.indice+1]    # faz o fim apontar pro dado inserido
                    else:   # caso o fim esteja antes do inicio
                        temp_indice = self.getTamanho() - (self.maximo - self.inicio.indice) # calcula o indice q será usado quando circula // maximo - inicio (10 - 8) = 2 = X --> tamanho (6) - X (2) = 4
                        #print(temp_indice)
                        temp_dado = Dado_da_Lista(nodo=posicao, indice=temp_indice, dado=dado, anterior=self.fim, proximo=self.inicio)   # cria um obj temporario
                        
                        self.fim.alteraProximo(temp_dado)   # faz o antigo fim apontar para o novo fim
                        self.inicio.alteraAnterior(temp_dado)   # faz o inicio apontar para o novo fim
                        self.lista[self.fim.indice+1] = temp_dado   # posicao da lista vira o temp_dado (insere o dado)
                        self.fim = self.lista[self.fim.indice+1]    # faz o fim apontar pro dado inserido

                        self.exibir_estrutura()
                    
                else:   # caso o fim+1 esteja fora dos limites
                    print(">Fora dos limites")
                    #print(self.fim.indice)
                    temp_dado = Dado_da_Lista(nodo=posicao, indice=0, dado=dado, anterior=self.fim, proximo=self.inicio)    # cria um obj temporario - indice 0 (inicio da lista fisica)
                    
                    self.fim.alteraProximo(temp_dado)   # faz o antigo fim apontar para o novo fim
                    self.inicio.alteraAnterior(temp_dado)   # faz o inicio apontar para o novo fim
                    self.lista[0] = temp_dado   # posicao da lista vira o temp_dado (insere o dado)
                    self.fim = self.lista[0]    # faz o fim apontar pro dado inserido

            else:   # caso a posiçao desejada seja uma já ocupada (ou é invalida)
                if (posicao > self.fim.nodo+1) or (0 > posicao):
                    print('Posição inválida')
                    return False
                print("> Posição ocupada. Vamos Arrumar")
                if self.inicio.indice < self.fim.indice:    # caso o inicio esteja antes do fim
                    print('inicio antes do fim') # caso normal (empurra pro lado) & caso extremo (empurrar pra fora dos limites)

                    posicao_desejada = self.getDadoFromNodo(posicao).indice # posicao_desejada = indice do dado naquela posicao
                    
                    # anterior vai ser o anterior do dado que estava na posicao anterior
                    temp_dado = Dado_da_Lista(nodo=posicao, indice=posicao_desejada, dado=dado, anterior=self.lista[posicao_desejada].getAnterior(), proximo=self.lista[posicao_desejada])   # cria um obj temporario
                    # exemplo no print abaixo:
                    #print(temp_dado.getAnterior().dado)
                    if posicao_desejada == self.fim.indice: # caso a posicao desejada seja o fim da lista lógica (posicao desejada = fim)
                        if self.fim.indice == (self.maximo-1):  # caso essa posição seja também o fim da lista física
                            self.fim.alteraNodo(1)  # aumenta o n_nodo (endereço logico) do fim em 1
                            self.fim.alteraIndice(-(self.maximo-1)) # zera o endereço fisico do fim (indice = 0)
                            self.lista[0] = self.fim    # coloca o fim no inicio da lista logica
                            self.lista[self.maximo-1] = temp_dado   # coloca o temp dado no final da lista logica
                            self.lista[posicao_desejada].getAnterior().alteraProximo(self.lista[posicao_desejada]) # faz o proximo do anterior apontar pro dado inserido
                            self.lista[posicao_desejada].getProximo().alteraAnterior(self.lista[posicao_desejada]) # faz o anterior do proximo apontar pro dado inserido
                        else:   # caso essa posição não seja o fim da lista física
                            self.fim.alteraNodo(1)  # aumenta o n_nodo (endereço logico) do fim em 1
                            self.fim.alteraIndice(1) # zera o endereço fisico do fim (indice = 0)
                            self.lista[posicao_desejada+1] = self.fim    # coloca o fim no inicio da lista logica
                            self.lista[posicao_desejada] = temp_dado    # insere o dado desejado na posicao desejada
                            self.lista[posicao_desejada].getAnterior().alteraProximo(self.lista[posicao_desejada]) # faz o proximo do anterior apontar pro dado inserido
                            self.lista[posicao_desejada].getProximo().alteraAnterior(self.lista[posicao_desejada]) # faz o anterior do proximo apontar pro dado inserido
                        return True

                    
                    else:   # caso a posicao desejada não seja o ultimo item da lista lógica (posicao desejada < fim)
                        if self.fim.indice == (self.maximo-1):  # caso o fim da lista lógica seja também o fim da lista física
                            self.fim.alteraNodo(1)  # aumenta o n_nodo (endereço logico) do fim em 1
                            self.fim.alteraIndice(-(self.maximo-1)) # zera o endereço fisico do fim (indice = 0)
                            self.lista[0] = self.fim    # coloca o fim no inicio da lista logica
                            
                            for i in range((self.maximo-1), posicao_desejada, -1):  # loop pra empurrar o lado direito da lista fisica:
                                self.lista[i] = self.lista[i-1] # empurra o endereço da lista fisica para direita
                                self.lista[i].alteraNodo(1) # aumenta o n_nodo (endereço lógico) em 1
                                self.lista[i].alteraIndice(1)   # aumenta o indice (endereço fisico) em 1
                            
                            self.lista[posicao_desejada] = temp_dado    # insere o dado desejado na posicao desejada
                            self.lista[posicao_desejada].getAnterior().alteraProximo(self.lista[posicao_desejada]) # faz o proximo do anterior apontar pro dado inserido
                            self.lista[posicao_desejada].getProximo().alteraAnterior(self.lista[posicao_desejada]) # faz o anterior do proximo apontar pro dado inserido
                        


                        else:   # caso o fim da lista lógica não seja o fim da lista física (fim < maximo-1)                            
                            for i in range((self.maximo-1), posicao_desejada, -1):  # loop pra empurrar o lado direito da lista fisica:
                                self.lista[i] = self.lista[i-1] # empurra o endereço da lista fisica para direita
                                self.lista[i].alteraNodo(1) # aumenta o n_nodo (endereço lógico) em 1
                                self.lista[i].alteraIndice(1)   # aumenta o indice (endereço fisico) em 1
                            # colocar o dado desejado na posição desejada:
                            self.lista[posicao_desejada] = temp_dado    # insere o dado desejado na posicao desejada
                            self.lista[posicao_desejada].getAnterior().alteraProximo(self.lista[posicao_desejada]) # faz o proximo do anterior apontar pro dado inserido
                            self.lista[posicao_desejada].getProximo().alteraAnterior(self.lista[posicao_desejada]) # faz o anterior do proximo apontar pro dado inserido
                        return True
                            
                    
                        
                        # loop para empurrar pro lado
                else:   # caso a lista circule (inicio após o fim)
                    print('fim antes do inicio')
                    
                    posicao_desejada = self.getDadoFromNodo(posicao).indice # posicao_desejada = indice do dado naquela posicao
                    
                    temp_dado = Dado_da_Lista(nodo=posicao, indice=posicao_desejada, dado=dado, anterior=self.lista[posicao_desejada-1], proximo=self.lista[posicao_desejada])   # cria um obj temporario
                    #proximo = posicao_desejada pois esse será empurrado pro lado, virando o próximo

                    print(posicao_desejada, self.fim.indice+1)

                    if posicao_desejada == self.fim.indice: # caso a posicao desejada seja o fim da lista circular
                        self.fim.alteraNodo(1)  # altera o nodo do fim
                        self.fim.alteraIndice(1)    # altera o indice do fim
                        self.lista[posicao_desejada+1] = self.lista[posicao_desejada]    # empurra o fim pro lado
                        self.lista[posicao_desejada] = temp_dado    # insere o dado desejado na posicao desejada
                        self.lista[posicao_desejada].getAnterior().alteraProximo(self.lista[posicao_desejada]) # faz o proximo do anterior apontar pro dado inserido
                        self.lista[posicao_desejada].getProximo().alteraAnterior(self.lista[posicao_desejada]) # faz o anterior do proximo apontar pro dado inserido
                        return True
                    
                    else:   # caso a posicao desejada nao esteja no fim da lista
                        if posicao_desejada >= self.inicio.indice:   # caso a posicao desejada seja antes da fronteira
                            print('>> caso empurra na fronteira')

                            ## loop pra empurrar o lado esquerdo da lista fisica:
                            for i in range((self.fim.indice+1), 0, -1):
                                #print(i)
                                self.lista[i] = self.lista[i-1] # empurra o endereço da lista fisica para direita
                                self.lista[i].alteraNodo(1) # aumenta o n_nodo (endereço lógico) em 1
                                self.lista[i].alteraIndice(1)   # aumenta o indice (endereço fisico) em 1
                            self.lista[0] = self.lista[self.maximo-1]   # empurra o ultimo da lista fisica para o inicio da lista fisica
                            self.lista[0].alteraNodo(1) # aumenta o n_nodo (endereço lógico) em 1
                            self.lista[0].alteraIndice(-(self.maximo-1))    # o indice (endereço fisico) vira 0
                            self.lista[self.maximo-1] = Dado_da_Lista(nodo=-1, indice=self.maximo-1)
                            ##

                            # loop pra empurrar o lado direito da lista fisica:
                            for i in range((self.maximo-1), posicao_desejada, -1):
                                self.lista[i] = self.lista[i-1] # empurra o endereço da lista fisica para direita
                                self.lista[i].alteraNodo(1) # aumenta o n_nodo (endereço lógico) em 1
                                self.lista[i].alteraIndice(1)   # aumenta o indice (endereço fisico) em 1
                            #
                            # colocar o dado desejado na posição desejada:
                            self.lista[posicao_desejada] = temp_dado    # insere o dado desejado na posicao desejada
                            self.lista[posicao_desejada].getAnterior().alteraProximo(self.lista[posicao_desejada]) # faz o proximo do anterior apontar pro dado inserido
                            self.lista[posicao_desejada].getProximo().alteraAnterior(self.lista[posicao_desejada]) # faz o anterior do proximo apontar pro dado inserido
                            return True


                        else:   # caso a posicao desejada seja após circular
                            print(posicao_desejada, self.fim.indice+1)
                            for i in range((self.fim.indice+1), posicao_desejada, -1):    # loop para empurrar (o i diminui)
                                print(i)
                                self.lista[i] = self.lista[i-1]
                            self.lista[posicao_desejada] = temp_dado    # insere o dado desejado na posicao desejada
                            self.lista[posicao_desejada].getAnterior().alteraProximo(self.lista[posicao_desejada]) # faz o proximo do anterior apontar pro dado inserido
                            self.lista[posicao_desejada].getProximo().alteraAnterior(self.lista[posicao_desejada]) # faz o anterior do proximo apontar pro dado inserido
                            return True
                            


    def remover(self, posicao):
        dado_remover = self.getDadoFromNodo(posicao)    # define o dado a ser removido a partir da posicao
        print(dado_remover.dado)

        antigo_proximo = dado_remover.getProximo()  # salva o antigo proximo do dado a ser removido
        antigo_anterior = dado_remover.getAnterior()    # salva o antigo anterior do dado a ser removido

        antigo_anterior.alteraProximo(antigo_proximo)  # faz o anterior apontar pro proximo do dado removido
        antigo_proximo.alteraAnterior(antigo_anterior) # faz o proximo apontar pro anterior do dado removido

        self.lista[dado_remover.indice] = Dado_da_Lista(nodo=-1, indice=i)  # remove o dado desejado

        # agora é preciso ajeitar a lista
        # >>>>>>>> FAZER

    def acessar(self):
        pass


    def exibir_estrutura(self):
        print("\n-- Lista:\n[", end="")
        for i in range(0, len(self.lista)):
            if self.lista[i] != None:  # --> só vai printar dados que não forem "None"
                if i < len(self.lista)-1:
                    print(f"{self.lista[i].dado}", end=", ")
                else:
                    print(f"{self.lista[i].dado}", end="]\n--\n")


    def buscar_info(self):
        pass
    def acessar_info(self):
        pass


# teste <<<
print()

lista = Lista_circular(10)
letras = ['A','B','C','D','E','F','G','H','I','J', 'teste']
lista.exibir_estrutura()

lista.inserir('A', 4)

for i in range(1, lista.maximo-2):
    lista.mostrar_dados()
    lista.inserir(letras[i], i)
    lista.exibir_estrutura()


lista.remover(4)
lista.mostrar_dados()
#Inserir, Remover, Acessar, Exibir estrutura, Buscar informação, Acessar informação
class Dado_da_Lista:    # classe utilizada para os NODOS da Lista Circular
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



class Lista_circular:   # classe que permite implementar uma Lista Circular
    def __init__(self, n_max):
        self.maximo = n_max

        
        self.lista = [None] * self.maximo
        for i in range(0, self.maximo):
            self.lista[i] = Dado_da_Lista(nodo=-1, indice=i)
        
        self.inicio = -1
        self.fim = -1


    def getDadoFromNodo(self, n_nodo):  # procura e retorna um objeto da lista (nodo) a partir de uma dada posição lógica
        for i in self.lista:
            if i.nodo == n_nodo:
                return i
        
        # caso ele nao ache a partir da posicao:
        for i in self.lista:    # acho que essa parte está obsoleta mas não tenho certeza então não vou mexer
            if i.nodo == n_nodo-1:
                return i

    
    def isVazia(self): # Verifica se a lista está vazia
        if type(self.inicio) == int:
            if self.inicio == -1 and self.fim == -1:
                return True
        return False

    
    def getTamanho(self):   # retorna o tamanho da lista lógica
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


    def isCheia(self):  # verifica se a lista está cheia
        if type(self.inicio) == int:
            return (self.fim == (self.inicio-1))
        else:
            return ((self.fim.nodo == (self.inicio.nodo-1))) or (self.inicio.nodo == 0 and self.fim.nodo == self.maximo-1)


    def mostrar_dados(self):    # função para chamar a função de classe "exibirSe()" dos nodos da lista lógica
        for i in self.lista:
                i.exibirSe()
        print(f'\ninicio da lista: {self.inicio.dado} \n final da lista: {self.fim.dado}')


    def inserir(self, dado, posicao: int=None): # função para inserir dados na lista, permitindo reposicionamento de outros dados caso necessário
    #OBS: caso o usuario não de uma posicao, o padrão será: A) 0 caso a lista esteja vazia; B) fim+1 caso não esteja vazia
        if self.isCheia():
            print('>>Erro: Lista cheia')
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
            return True
        
        else:   # caso nao esteja vazia--> aqui a posição será o nodo desejado
            if posicao == None:
                posicao = self.fim.nodo+1   # escolhe a posicao padrao fim+1

            if posicao == self.fim.nodo+1:  # caso a posicao desejada seja fim+1
                if self.fim.indice < (self.maximo-1):   # testa se o fim+1 está dentro dos limites
                    temp_indice = self.fim.indice+1 #self.getTamanho() - (self.maximo - self.inicio.indice) # calcula o indice q será usado quando circula // maximo - inicio (10 - 8) = 2 = X --> tamanho (6) - X (2) = 4
                    temp_dado = Dado_da_Lista(nodo=posicao, indice=temp_indice, dado=dado, anterior=self.fim, proximo=self.inicio)   # cria um obj temporario
                    
                    self.fim.alteraProximo(temp_dado)   # faz o antigo fim apontar para o novo fim
                    self.inicio.alteraAnterior(temp_dado)   # faz o inicio apontar para o novo fim
                    self.lista[self.fim.indice+1] = temp_dado   # posicao da lista vira o temp_dado (insere o dado)
                    self.fim = self.lista[self.fim.indice+1]    # faz o fim apontar pro dado inserido
                else:   # caso o fim+1 esteja fora dos limites
                    #print(">Fora dos limites")
                    temp_dado = Dado_da_Lista(nodo=posicao, indice=0, dado=dado, anterior=self.fim, proximo=self.inicio)    # cria um obj temporario - indice 0 (inicio da lista fisica)
                    
                    self.fim.alteraProximo(temp_dado)   # faz o antigo fim apontar para o novo fim
                    self.inicio.alteraAnterior(temp_dado)   # faz o inicio apontar para o novo fim
                    self.lista[0] = temp_dado   # posicao da lista vira o temp_dado (insere o dado)
                    self.fim = self.lista[0]    # faz o fim apontar pro dado inserido

            else:   # caso a posiçao desejada seja uma já ocupada (ou é invalida)
                if (posicao > self.fim.nodo+1) or (0 > posicao):
                    print('> Erro: Posição inválida')
                    return False
                #print("> Posição ocupada. Vamos Arrumar")
                if self.inicio.indice < self.fim.indice:    # caso o inicio esteja antes do fim
                    #print('inicio antes do fim') # caso normal (empurra pro lado) & caso extremo (empurrar pra fora dos limites)

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
                    #print('fim antes do inicio')
                    
                    posicao_desejada = self.getDadoFromNodo(posicao).indice # posicao_desejada = indice do dado naquela posicao
                    
                    temp_dado = Dado_da_Lista(nodo=posicao, indice=posicao_desejada, dado=dado, anterior=self.lista[posicao_desejada-1], proximo=self.lista[posicao_desejada])   # cria um obj temporario
                    #proximo = posicao_desejada pois esse será empurrado pro lado, virando o próximo


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
                            #print('>> caso empurra na fronteira')

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
                            #print(posicao_desejada, self.fim.indice+1)
                            for i in range((self.fim.indice+1), posicao_desejada, -1):    # loop para empurrar (o i diminui)
                                #print(i)
                                self.lista[i] = self.lista[i-1]
                            self.lista[posicao_desejada] = temp_dado    # insere o dado desejado na posicao desejada
                            self.lista[posicao_desejada].getAnterior().alteraProximo(self.lista[posicao_desejada]) # faz o proximo do anterior apontar pro dado inserido
                            self.lista[posicao_desejada].getProximo().alteraAnterior(self.lista[posicao_desejada]) # faz o anterior do proximo apontar pro dado inserido
                            return True
                            

    def remover(self, posicao): # função para remover dados da lista, permitindo reposicionamento de outros dados caso necessário
        if self.isVazia():
            print("Erro: Lista Vazia.")
            return False
        if 0 > posicao > self.getTamanho():
            print("Erro: Posição inválida")
            return False
        dado_remover = self.getDadoFromNodo(posicao)    # define o dado a ser removido a partir da posicao
        #print(dado_remover.dado)

        if self.getTamanho() > 1:   # testa se a lista tem mais de um item
            #muda_inicio = False
            if dado_remover == self.inicio: # testa se o dado a ser removido é o item inicial
                #muda_inicio = True
                self.inicio = dado_remover.getProximo() # o inicio vai ser o proximo
                self.lista[dado_remover.indice] = Dado_da_Lista(nodo=-1, indice=dado_remover.indice)  # remove o dado desejado
                muda_nodo = dado_remover.getProximo()   # variavel para diminuir o n_posicao de todos da lista
                muda_nodo.alteraNodo(-1)    #   nodo-- (posicao--)
                muda_nodo = muda_nodo.getProximo()  # proximo nodo
                while muda_nodo != self.inicio:    # enquanto o proximo nodo nao for o IL
                    muda_nodo.alteraNodo(-1)    #   nodo-- (posicao--)
                    muda_nodo = muda_nodo.getProximo()  # proximo nodo
                return True
        else:   # se a lista tiver apenas um item, apenas deleta o item e segue a vida
            self.lista[dado_remover.indice] = Dado_da_Lista(nodo=-1, indice=dado_remover.indice)  # remove o dado desejado
            return True
        
        antigo_proximo = dado_remover.getProximo()  # salva o antigo proximo do dado a ser removido
        antigo_anterior = dado_remover.getAnterior()    # salva o antigo anterior do dado a ser removido

        antigo_anterior.alteraProximo(antigo_proximo)  # faz o anterior apontar pro proximo do dado removido
        antigo_proximo.alteraAnterior(antigo_anterior) # faz o proximo apontar pro anterior do dado removido

        self.lista[dado_remover.indice] = Dado_da_Lista(nodo=-1, indice=dado_remover.indice)  # remove o dado desejado

        '''if dado_remover == self.fim:  # testa se o dado a ser removido é o fim da lista lógica
            self.fim = antigo_anterior
            muda_fim = False'''

        # agora é preciso ajeitar a lista
        # >>>>>>>> FAZER
        dado_empurra = antigo_proximo   # o o dado a ser empurrado é o proximo do removido

        while dado_empurra != self.inicio:   # enquanto o dado_empurra não é um None se o proximo for o inicio, ele nao empurra
            
            if dado_empurra.indice == 0:    # se o indice for 0, empurra pro final da lista fisica
                dado_empurra.alteraIndice(self.maximo-1)    # indice do dado a ser empurrado vira maximo-1
            else:   # se o indice nao for 0, o indice diminui em 1 (indice--)
                dado_empurra.alteraIndice(-1)   # indice--
            dado_empurra.alteraNodo(-1) # n_nodo--
            self.lista[dado_empurra.indice] = dado_empurra  # coloca o dado a ser empurrado na posição desejada

            '''
            if muda_inicio: # caso o dado removido fosse o inicio
                self.inicio = self.lista[dado_empurra.indice]
                muda_inicio = False'''
            

            dado_empurra = self.lista[dado_empurra.indice].getProximo() # o o dado a ser empurrado é o proximo do empurrado

            if self.lista[dado_empurra.indice].getProximo() == self.fim:
                self.lista[self.lista[dado_empurra.indice].getProximo().indice] = Dado_da_Lista(nodo=-1, indice=(dado_empurra.getProximo().indice))  # remove o dado desejado
                #self.lista[dado_empurra.indice].getProximo() = Dado_da_Lista(nodo=-1, indice=(dado_empurra.getProximo().indice))  # remove o dado desejado
                #self.fim = self.lista[dado_empurra.indice] # torna esse o fim da lista lógica


        #self.mostrar_dados()
        for i in range(0, self.maximo): # loop pra verificar se tem repetidos
            if i+1 < (self.maximo): # verifica se o i+1 nao sai da fronteira
                if self.lista[i] == self.lista[i+1]:    # se lista[i] == lista[i+1]
                    self.lista[i+1] = Dado_da_Lista(nodo=-1, indice=((self.lista[i].getProximo().indice)-1))    # apaga o repetido
            else:
                if self.lista[i] == self.lista[0]:    # se lista[i] == lista[0]
                    self.lista[0] = Dado_da_Lista(nodo=-1, indice=((self.lista[i].getProximo().indice)-1))    # apaga o repetido
        return True

    
    def exibir_estrutura(self, vazios: bool=False): # exibe a lista lógica. Permite mostrar os espaços vazios caso desejado
        print("\n-- Lista:\n[ ", end="")

        if vazios:  # caso True, ele mostra os "None" (endereços vazios) da lista
            for i in range(0, self.maximo): 
                if i < self.maximo-1:
                    if (self.lista[i] == self.inicio) and (self.lista[i] == self.fim):
                        print(f"<{self.lista[i].dado}", end="> ")
                    elif self.lista[i] == self.fim:
                        print(f"{self.lista[i].dado}", end="> ")
                    elif self.lista[i] == self.inicio:
                        print(f"<{self.lista[i].dado}", end=", ")
                    else:
                        print(f"{self.lista[i].dado}", end=", ")
                else:
                    if (self.lista[i] == self.inicio) and (self.lista[i] == self.fim):
                        print(f"<{self.lista[i].dado}", end="> ]")
                    elif self.lista[i] == self.fim:
                        print(f"{self.lista[i].dado}", end="> ]")
                    elif self.lista[i] == self.inicio:
                        print(f"<{self.lista[i].dado}", end=" ]")
                    else:
                        print(f"{self.lista[i].dado}", end=" ]")
        
        else:   # caso False (padrão), ele mostra apenas a lista lógica (apenas os nodos)
            for i in range(0, self.maximo):
                if self.lista[i].nodo != (-1):  # --> só vai printar dados que não forem "None"
                    if i < self.maximo-1:
                        if (self.lista[i] == self.inicio) and (self.lista[i] == self.fim):
                            print(f"<{self.lista[i].dado}", end="> ")
                        elif self.lista[i] == self.fim:
                            print(f"{self.lista[i].dado}", end="> ")
                        elif self.lista[i] == self.inicio:
                            print(f"<{self.lista[i].dado}", end=", ")
                        else:
                            print(f"{self.lista[i].dado}", end=", ")
                    else:
                        if (self.lista[i] == self.inicio) and (self.lista[i] == self.fim):
                            print(f"<{self.lista[i].dado}", end="> ")
                        elif self.lista[i] == self.fim:
                            print(f"{self.lista[i].dado}", end="> ")
                        elif self.lista[i] == self.inicio:
                            print(f"<{self.lista[i].dado}", end=" ")
                        else:
                            print(f"{self.lista[i].dado}", end=" ")
            print(']', end='')
        print()

    def buscar_info(self, posicao): # função para buscar um dado de um nodo a partir de dada posição
        info = self.getDadoFromNodo(posicao)
        return info.dado


    def acessar_info(self, posicao): # função para buscar e exibir a estrutura de um nodo a partir de dada posição
        info = self.getDadoFromNodo(posicao)
        print(info.exibirSe())
        return True


# teste <<<

# para ver apenas os nodos ocupados da lista, use a função listaX.exibir_estrutura()
# para ver os nodos vazios da lista, use a mesma função, com o parâmetro "vazios=True" --> listaX.exibir_estrutura(vazios=True)
# OBS: o padrão é vazios=False


# para ver analisar os nodos da lista, use listaX.mostrar_dados() --> printa cada estrutura de nodo em linhas separadas


print()

lista_teste = Lista_circular(10)
letras = ['A','B','C','D','E','F','G','H','I','J', 'teste']
lista_teste.exibir_estrutura(vazios=True)

lista_teste.inserir('A')
lista_teste.exibir_estrutura(vazios=True)


#OBS:   Esses símbolos    < >   representam inicio e fim da lista lógica, respectivamente
# ou seja,    < = inicio  //   > = fim


# 1) Povoamento Inicial: Inserir elementos até que a lista ocupe o final do arranjo.
for i in range(1, len(letras)):
    lista_teste.inserir(letras[i])
    lista_teste.exibir_estrutura(vazios=True)


# 2) Geração de Espaço: Remover os primeiros elementos para deslocar o IL.
for i in range(0, 4):
    lista_teste.remover(0)
    lista_teste.exibir_estrutura(vazios=True)

# 3) Teste de Circularidade: Inserir um elemento na última posição lógica para forçar o ponteiro FL a retornar ao início do arranjo (IA).
lista_teste.inserir('teste3', 6)
lista_teste.exibir_estrutura(vazios=True)

# 4) O Teste Crítico (Inserção no Meio): Com a lista "quebrada" (parte no fim do vetor e parte no início), realizar uma inserção em
# uma posição central e demonstrar que o deslocamento não corrompeu a ordem dos dados.
lista_teste.inserir('teste4', 4)
lista_teste.exibir_estrutura(vazios=True)

lista_teste.inserir('teste5', 5)
lista_teste.exibir_estrutura(vazios=True)

lista_teste.inserir('teste6', 2)
lista_teste.exibir_estrutura(vazios=True)

lista_teste.exibir_estrutura()

lista_exemplar = Lista_circular(10)




print('\n\n\n Agora uma lista mais bonita:')
lista_exemplar.inserir('A', 5)

for i in range(1, len(letras)-3):
    lista_exemplar.inserir(letras[i])

lista_exemplar.exibir_estrutura()

lista_exemplar.mostrar_dados()

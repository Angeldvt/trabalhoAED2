#Inserir, Remover, Acessar, Exibir estrutura, Buscar informação, Acessar informação
class Dado_da_Lista:
    def __init__(self, nodo, dado=None, anterior=None, proximo=None):
        self.dado_anterior = anterior
        self.dado_proximo = proximo
        self.dado = dado
        self.nodo = nodo
    def alteraProximo(self, proximo):
        self.dado_proximo = proximo
    def alteraAnterior(self, anterior):
        self.dado_anterior = anterior
    def alteraNodo(self, n):
        self.nodo += n

    def getProximo(self):
        return self.dado_proximo
    
    def getAnterior(self):
        return self.dado_anterior

    def exibirSe(self):
        print(f'[ dado: {self.dado} / nodo: {self.nodo}', end=' / ')

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
            self.lista[i] = Dado_da_Lista(nodo=-1)
        
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


    # Verifica se a lista está vazia
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


    def inserir(self, dado, posicao: int=None):
        if self.isCheia():
            print('>>Lista cheia')
            return False
        
        if self.isVazia():
            if posicao == None:
                posicao = 0
            #else:
                #posicao -= 1
            temp_proximo = self.lista[posicao].getProximo()
            temp_anterior = self.lista[posicao].getAnterior()
            self.lista[posicao] = Dado_da_Lista(nodo=0, dado=dado, anterior=temp_anterior, proximo=temp_proximo)
            self.lista[posicao].getAnterior().alteraProximo(self.lista[posicao])
            self.lista[posicao].getProximo().alteraAnterior(self.lista[posicao])
            self.inicio = self.lista[posicao]
            self.fim = self.lista[posicao]

            '''
            temp = 1
            anota_nodo = False
            for i in range(0, self.maximo):
                if anota_nodo:
                    self.lista[i].nodo = temp
                    temp += 1
                if self.lista[i].nodo == 0:
                    anota_nodo = True
            
            for i in range(0, self)
            '''
            n_nodo = 2
            proximo_nodo = self.lista[posicao].getProximo()
            while proximo_nodo.nodo != 0:
                proximo_nodo.alteraNodo(n_nodo)
                proximo_nodo = proximo_nodo.getProximo()
                n_nodo += 1
                #print(proximo_nodo.nodo)
            
            print("fim.dado/posicao:", self.fim.dado, self.fim.nodo)
            return True

        else:   # aqui a posição será o nodo desejado
            for i in self.lista:
                if posicao == i.nodo:
                    i.exibirSe()


            '''
            if posicao == None:
                posicao = self.getTamanho()+self.inicio.nodo
                print(posicao)
            
            if posicao < 0:
                print('posicao inválida')
                return False
            
            if self.lista[posicao].dado == None:  # caso simples (caso a posição desejada esteja vazia)
                print("aqui tem nada")
                temp_proximo = self.lista[posicao].getProximo()
                temp_anterior = self.lista[posicao].getAnterior()
                self.lista[posicao] = Dado_da_Lista(nodo=posicao, dado=dado, anterior=temp_anterior, proximo=temp_proximo)
                self.lista[posicao].getAnterior().alteraProximo(self.lista[posicao])
                self.lista[posicao].getProximo().alteraAnterior(self.lista[posicao])
                if posicao == self.getTamanho():
                    self.fim = self.lista[posicao]
                    print("fim.dado:", self.fim.dado)

                if lista.isVazia():
                    self.inicio = self.lista[posicao]
                    self.fim = self.lista[posicao]
                    print("fim.dado:", self.fim.dado)
                return True
            else:   # caso a posição desejada não esteja vazia
                print('Aqui tem coisa, vamos arrumar')  # precisaremos testar: se o inicio muda; se o fim muda; se o fim/inicio circulam pelo arranjo
                #if 
            '''    

            




    def remover(self):
        pass
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

lista.exibir_estrutura()

lista.inserir(1, 5)
lista.exibir_estrutura()

for i in lista.lista:
    i.exibirSe()


print('\n\n')
lista.inserir(2, 1)

lista.exibir_estrutura()
#lista.exibir_estrutura()

#for i in lista.lista:
    #i.exibirSe()
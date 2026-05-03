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

class Lista_circular:
    def __init__(self, n_max):
        self.maximo = n_max

        
        self.lista = [None] * self.maximo
        for i in range(0, self.maximo):
            self.lista[i] = Dado_da_Lista(nodo=i+1)
        
        self.inicio = -1
        self.fim = -1


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
            return self.maximo - self.inicio + self.fim + 1 # retorna tamanho da lista circular
            #           10      -       9     +     8)   + 1     [L4,L5,L6,L7,L8,L9,L10,L1,L2,L3]

    def isCheia(self):
        return (self.fim == (self.inicio-1))


    def inserir(self, dado, posicao: int=None):
        if self.isCheia():
            print('>>Lista cheia')
            return False
        
        if self.isVazia():
            if not posicao:
                posicao = 0
            else:
                posicao -= 1
            self.lista[posicao] = Dado_da_Lista(nodo=posicao, dado=dado,)
            self.inicio = posicao
            self.fim = posicao
            return True

        else:
            if posicao == None:
                posicao = self.getTamanho()+1
                print(posicao)
                #if (posicao-1) > 0: # não lembro o objetivo desse teste
                if self.lista[posicao-1].dado == None:  # caso simples
                    print("aqui tem nada")
                    self.lista[posicao-1] = Dado_da_Lista(nodo=posicao, dado=dado, anterior=self.lista[posicao-2], proximo=self.lista[posicao])
                    self.lista[posicao-2].alteraProximo(self.lista[posicao-1])  # faz o anterior apontar pro atual
                    self.lista[posicao].alteraAnterior(self.lista[posicao-1])   # faz o proximo apontar pro atual
                    self.fim += 1
                    return True
            
            if posicao > 0:
                pass




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

lista.inserir(1)

lista.exibir_estrutura()
print(lista.inicio, lista.fim) # ---> quando tiver 1 elemento, ambos devem ter o mesmo valor


lista.inserir(2)
lista.exibir_estrutura()
print(lista.inicio, lista.fim) # ---> quando tiver 1 elemento, ambos devem ter o mesmo valor

print("item 2 (indice 1) da lista aponta pro dado anterior:", lista.lista[1].dado_anterior.dado)
print("item 2 (indice 1) da lista aponta pro próximo dado:", lista.lista[1].dado_proximo.dado)
print("item 1 (indice 0) da lista aponta pro próximo dado:", lista.lista[0].dado_proximo.dado)
print("item 3 (indice 2) da lista aponta pro dado anterior:", lista.lista[2].dado_anterior.dado)


lista.inserir(3)

lista.exibir_estrutura()
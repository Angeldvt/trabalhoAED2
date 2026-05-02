#Inserir, Remover, Acessar, Exibir estrutura, Buscar informação, Acessar informação

class lista_linear:
    def __init__(self, n_max):
        self.tamanho = n_max
        self.lista = [None] * self.tamanho
        self.inicio = 9
        self.fim = 8


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
            #           10   -   9     +     8) + 1     [L4,L5,L6,L7,L8,L9,L10,L1,L2,L3]

    def isCheia(self):
        return (self.fim == (self.inicio-1))



    def inserir(self):
        pass
    def remover(self):
        pass
    def acessar(self):
        pass
    def exibir_estrutura(self):
        pass
    def buscar_info(self):
        pass
    def acessar_info(self):
        pass


# teste <<<
lista = lista_linear(10)
print(lista.isVazia())
print(lista.getTamanho())

print(lista.isCheia())


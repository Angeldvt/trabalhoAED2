class Lista:
    def __init__(self, max):
        self.max = max
        self.vetor = [None] * self.max
        self.ini = -1
        self.fim = -1
  
    def Vazia(self):
        return self.ini == -1 and self.fim == -1
    #retorna true ou false

    def Tamanho(self):
        if self.Vazia():
            return 0
        else:
            return self.fim - self.ini + 1

    def Cheia(self):
        return self.ini==0 and self.fim==self.max-1
    #retorna um true ou false 
    
    def Inserir(self, posicao, dado):   #var posicao e var dado vem de fora
        if ((not self.Cheia()) and posicao > 0 and posicao <= self.Tamanho()+1):
            if (self.Vazia()):
                self.ini = 0
                self.fim = 0
            elif (self.fim != self.max - 1):                  
                for i in range(self.fim, self.ini + posicao -2, -1):
                    self.vetor[i+1] = self.vetor[i]
                    print("moveu direita")
                self.fim = self.fim + 1
            else: 
                for i in range(self.ini, self.ini + posicao - 1): 
                    self.vetor[i-1] = self.vetor[i]
                    print("moveu esquerda")
                self.ini = self.ini - 1
            self.vetor[self.ini + posicao - 1] = dado
            return True
        else:
            print("Não foi possível inserir, lista Cheia ou posição inválida")
            return False
    
    def Consultar(self, posicao):
        if self.Vazia() or posicao < 1 or posicao > self.Tamanho():
            return None
        return self.vetor[self.ini + posicao - 1]
    
    def Limpar(self):
        self.vetor = [None] * self.max
        self.ini = -1
        self.fim = -1

    def Remover(self, posicao):
        if self.Vazia() or posicao < 1 or posicao > self.Tamanho():
            return False

        indice = self.ini + posicao - 1
        # decide o menor custo
        if posicao <= self.Tamanho() // 2:
            # desloca para a direita
            for i in range(indice, self.ini, -1):
                self.vetor[i] = self.vetor[i - 1]
            self.vetor[self.ini] = None
            self.ini += 1
        else:
            # desloca para a esquerda
            for i in range(indice, self.fim):
                self.vetor[i] = self.vetor[i + 1]
            self.vetor[self.fim] = None
            self.fim -= 1

        if self.ini > self.fim:
            self.ini = -1
            self.fim = -1

        return True
        
    def Exibir(self):        
        print(f"[", end=' ')
        for i in range(self.ini, self.fim+1):
            print(f"{self.vetor[i]}", end=' ')
            if i <self.fim:
                print("-", end=' ')
        print(f"]", end=' ')
        print("\n-------------")

    def InserirOtimizado(self, posicao, dado):
        # verificar se existe espaço e se a posição é válida
        if (not self.Cheia()) and posicao > 0 and posicao <= self.Tamanho()+1:
            if (self.Vazia()):
                self.ini = self.max // 2
                self.fim = self.max // 2
                indice = self.ini
            # se for no início e exitir espaço
            elif posicao == 1 and self.ini != 0:
                self.ini = self.ini - 1
                indice = self.ini
            # se for no fim e existir espaço
            elif posicao > self.Tamanho() and self.fim != self.max - 1:
                self.fim = self.fim + 1
                indice = self.fim
            else:
                # se não tem espaço no início, ou se custo é menor deslocando para o fim e ainda existe espaço
                if self.ini == 0 or (posicao > self.Tamanho() // 2 and self.fim != self.max - 1):
                    for i in range(self.fim, self.ini + posicao - 2, -1): # deslocar para o fim
                        self.vetor[i+1] = self.vetor[i]
                    self.fim = self.fim + 1
                else: # deslocar para o início
                    for i in range(self.ini, self.ini + posicao - 1):
                        self.vetor[i-1] = self.vetor[i]
                    self.ini = self.ini - 1
                indice = self.ini + posicao - 1
            self.vetor[indice] = dado
            return True
        else:
            return False
        

lista = Lista(10)

lista.Inserir(1, 'teste1')
lista.Exibir()
print(f'lista.ini: {lista.ini} // lista.fim: {lista.fim}')

lista.Inserir(2, 'teste2')
lista.Exibir()
print(f'lista.ini: {lista.ini} // lista.fim: {lista.fim}')

for i in range(3, 11):
    lista.Inserir(i, f'teste{i}')

lista.Exibir()
print(f'lista.ini: {lista.ini} // lista.fim: {lista.fim}')
#print(lista)
print(lista.Cheia())
lista.Remover(1)
print(f'lista.ini: {lista.ini} // lista.fim: {lista.fim}')
lista.Exibir()
#  Importando as bibliotecas necessárias

import numpy as np # Para calcular a altura da árvore

def retirar_nulos_final(lst: list) -> list:
    """Função auxiliar para a função  build_max_heap e to_array

    Args:
        lst (list): list de objetos ou valores 

    Returns:
        _type_: _description_
    """
    sublista = []

    for i in range(len(lst)):
        # Verifica se o elemento é numérico 
        if isinstance(lst[i], (int, float)):
            # Atualiza a sublista com os elementos numéricos
            sublista = lst[:i + 1]

    # Remove os elementos `None` do final da sublista
    while sublista and sublista[-1] is None:
        sublista.pop()

    return sublista

 
def getcol(h: int) -> int:
    """função que determina a quantidade de colunas que vampos 
    precisar para o print tree

    Args:
        h (_type_): _description_

    Returns:
        _int_: número de colunas 
    """
    if h == 1:
        return 1
    return getcol(h-1) + getcol(h-1) + 1

class ArvoreBinaria:
    """Instance a ArvoreBinaria object 
    
    Arg:
        valor (falor): valor do nó 
    """
    
    def __init__(self, valor: float) -> None:
        self.valor  = valor
        self.filha_direita = None
        self.filha_esquerda = None 

    def __str__(self):
         valor_str = f"Valor: {self.valor}"
         filha_esquerda_str = f"Filha Esquerda: {self.filha_esquerda.valor if self.filha_esquerda else None}"
         filha_direita_str = f"Filha Direita: {self.filha_direita.valor if self.filha_direita else None}"
        
         return f"{valor_str}. {filha_esquerda_str}. {filha_direita_str}"
    
    def heapify(self) -> None:
        """método para transformar a árvore em um heap.
        """
        largest = self
        
        l = self.filha_esquerda
        r = self.filha_direita
        
        if not l is None and l.valor > largest.valor:
            largest = l 
        
        if not r is None and r.valor > largest.valor:
            largest = r
        
        if largest.valor != self.valor:
            self.valor, largest.valor =  largest.valor, self.valor
            largest.heapify()

    
    def buildmaxheap(self)-> None:
        """Método que aplica o heapify em toda a árvore

        Returns:
            _type_: _description_
        """
        # Tamanho da lista
        n = len(self.to_array())
        
        for i in range(n//2, -1, -1): #Começa a partir do último nó não-folha e vai até o primeiro
            if self.to_array_object()[i] is None:
                pass
            else:
                self.to_array_object()[i].heapify()
        

        return self.to_array
    
    def altura(self) -> int:
        """Método que retorna a altura da árvore

        Returns:
            altura (int) : altura da árvore
        """
        altura =  int(np.log2(len(self.to_array())))  + 1
        
        return altura
        
    def print_tree_aux(self, M: list, root: float, col: int, row: int, height: int)-> None:
        """_summary_

        Args:
            M (list): Matriz com os elementos que serão apresentados no print_tree
            root (float): valor do nó
            col (int): número de colunas
            row (int): número de linhas
            height (int): altura da árvore
        """
        if root is None:
            return
        
        M[row][col] = root.valor # Determiando o valor do elemento da matriz 
        self.print_tree_aux(M, root.filha_esquerda, col-pow(2, height-2), row+1, height-1)
        self.print_tree_aux(M, root.filha_direita, col+pow(2, height-2), row+1, height-1)
 
    def print_tree(self) -> None:
        """imprime uma representação gráfica da árvore na tela.

        Returns:
            str: _description_
        """
        h = self.altura()
        col = getcol(h)
        M = [[0 for _ in range(col)] for __ in range(h)]
        self.print_tree_aux(M, self, col//2, 0, h)
        
        print("****FELIZ NATAL JULIANO****")
        for i in M:
            for j in i:
                if j == 0:
                    print(" ", end=" ") # Espaços entre  os nós 
                else:
                    print(j, end=" ")
            print("")
        
    def to_array_object(self, tamanho_maximo=100) -> list:
        """converte a árvore na representação de array de objetos ArvoreBinaria.

        Args:
            tamanho_maximo (int, optional): tamanho do array que será retornado. Defaults to 100.

        Returns:
            array (lista): arvore na forma de lista de objetos da forma Arvore Binaria
        """
        array = [None] * tamanho_maximo  # Definindo a lista                 
        self._preencher_array_em_ordem_recursivo_objeto(array, 0)

        return array

    def to_array(self, tamanho_maximo=100) -> list:
        """converte a árvore na representação de array de valores numeros (int, float)

        Args:
            tamanho_maximo (int, optional): _description_. Defaults to 100.

        Returns:
            list: _description_
        """
        array = [None] * tamanho_maximo  # Definindo a lista                 
        self._preencher_array_em_ordem_recursivo_valor(array, 0)
        array = retirar_nulos_final(array)
        
        return array
    
    def _preencher_array_em_ordem_recursivo_valor(self, array: list, indice: int) -> None:
        """Método que adiciona os nós nas suas posiçoões, assim também
        como as filhas a esquerda e as filhas a direita, de forma recursiva

        Args:
            array (list): array que será modificado
            indice (int): indice da nó atual
        """
        if self is not None:
            
            array[indice] = self.valor
            if self.filha_esquerda is not None:
                self.filha_esquerda._preencher_array_em_ordem_recursivo_valor(array, 2 * indice + 1)
            if self.filha_direita is not None:
                self.filha_direita._preencher_array_em_ordem_recursivo_valor(array, 2 * indice + 2)

    def _preencher_array_em_ordem_recursivo_objeto(self, array: list, indice: int) -> None:
        """Método que adiciona os nós nas suas posiçoões, assim também
        como as filhas a esquerda e as filhas a direita, de forma recursiva

        Args:
            array (list): array que será modificado
            indice (int): indice da nó atual
        """
        if self is not None:
            
            array[indice] = self
            if self.filha_esquerda is not None:
                self.filha_esquerda._preencher_array_em_ordem_recursivo_objeto(array, 2 * indice + 1)
            if self.filha_direita is not None:
                self.filha_direita._preencher_array_em_ordem_recursivo_objeto(array, 2 * indice + 2)


def construir_arvore(array) -> ArvoreBinaria:
    """Recebe uma lista na forma de array e construa e retorne uma árvore
    com a classe ArvoreBinaria

    Args:
        array (list): Lista com os valores a serem transformados em árvore

    Returns:
        arvore: Lista com os nós
    """
    tamanho_array = len(array)
    
    for i in range(len(array)):
    
        if type(array[i]) == int:
            node = ArvoreBinaria(array[i])
            array[i] = node
        else:
            node = array[i]
       
        if 2*i+1 <tamanho_array:
            filha_esquerda = ArvoreBinaria(array[2*i+1])
            node.filha_esquerda = filha_esquerda
            array[2*i+1] = filha_esquerda
          
        if 2*i+2  <tamanho_array:
            
            filha_direita = ArvoreBinaria(array[2*i+2])
            node.filha_direita = filha_direita
            array[2*i+2] = filha_direita
    
    arvore = array[0]
    
    return arvore

##This Code is By JaimeWillianCarneiro

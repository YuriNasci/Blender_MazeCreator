import random

class Maze:
    maze = ''
    lin = col = 0;
    #--------------------------------------------------------------------
    # Procedimento que monta o labirinto, a partir de uma heurística.
    #--------------------------------------------------------------------
    
    def __init__(self, linhas, colunas):
        self.maze = {}
        self.lin = linhas
        self.col = colunas
        BAIXO, DIREITA, CIMA, ESQUERDA = 0, 1, 2, 3
        pilhaCaminhoSeguido = []
        podeConstruir = True
        # Definindo os valores iniciais de "x" e "y":
        #  - O valor de "x" será definido de forma completamente aleatória (de 0 ao número de linhas)
        x = xInicio = random.randrange(0, self.lin)
        #  - Já o valor de "y" será influenciado pelo valor de "x"
        #  - Se o valor de x for 0 ou o "número de linhas - 1" quer dizer que será uma borda então o valor de y não deve gerar uma diagonal
        y = yInicio = random.randrange(1, self.col - 1) if (x == 0 or x == self.lin - 1) else random.randrange(0,2) * (self.col - 1)
        self.maze[x, y] = 1
        
        # Enquanto o labirinto ainda puder ser construido, repete...
        while (podeConstruir):
            direcoesValidas = []
            #Heuristica: as posicoes candidatas para próxima posicao
            # tem 4 paredes ao seu redor e ainda não é um caminho.
            if(not self.isBorda(x, y) or (x == xInicio and y == yInicio)):
                if(self.numParedes(x, y - 2) == 4):
                    direcoesValidas.append(ESQUERDA)
                
                if(self.numParedes(x + 2, y) == 4):
                    direcoesValidas.append(BAIXO)
                    
                if(self.numParedes(x, y + 2) == 4):
                    direcoesValidas.append(DIREITA)
                
                if(self.numParedes(x - 2, y) == 4):
                    direcoesValidas.append(CIMA)
            # Se foi encontrada pelo menos uma posicao candidata,
            # escolhe aleatoriamente uma dessas posicoes e move para lá.
            candidatas = len(direcoesValidas)
            if (candidatas):
                direcaoEscolhida = direcoesValidas[random.randrange(0, candidatas)]
                if (direcaoEscolhida == BAIXO):
                    self.maze[x + 2, y] = self.maze[x + 1, y] = 1
                    x += 2
                elif (direcaoEscolhida == DIREITA):
                    self.maze[x, y + 2] = self.maze[x, y + 1] = 1
                    y += 2
                elif (direcaoEscolhida == CIMA):
                    self.maze[x - 2, y] = self.maze[x - 1, y] = 1
                    x -= 2
                elif (direcaoEscolhida == ESQUERDA):
                    self.maze[x, y - 2] = self.maze[x, y - 1] = 1
                    y -= 2
                
                # Agora, empilha a direcao escolhida
                pilhaCaminhoSeguido.append(direcaoEscolhida)            
            # fim do if
            # Agora, se não foi encontrada nenhuma posicao candidata, atualiza a posicao atual a partir da direcao 
            # armazenada no topo da pilha que contem o caminho seguido
            # Se a pilha está vazia, a construcao deve parar...
            elif (not pilhaCaminhoSeguido):
                podeConstruir = False
            # Senão, atualiza a posicao atual, voltando...
            else:
                volta = pilhaCaminhoSeguido.pop()
                if (volta == BAIXO):
                    x -= 2 
                elif (volta == DIREITA):
                    y -= 2
                elif (volta == CIMA):
                    x += 2
                elif(volta == ESQUERDA):
                    y += 2
    
    #----------------------------------------------------------------
    # Funcao usada para saber se a posicao está dentro do labirinto
    #----------------------------------------------------------------
    def isDentroLabirinto(self, i, j):
        if (i < self.lin and i >= 0 and j < self.col and j >= 0):
            return True
        else:
            return False
    #--------------------------------------------------------------------
    # Funcao usada para saber se a posicao denota uma borda do labirinto
    # -------------------------------------------------------------------
    def isBorda(self, i, j):
        if (i <= 0) or (i >= self.lin) or (j <=0) or (j >= self.col):
            return True
        else:
            return False
    #--------------------------------------------------------------------
    # Funcao usada para saber o número de parede ao redor de uma posição
    # --------------------------------------------------------------------
    def numParedes(self, i, j):
        n = 4
        
        if (not self.isDentroLabirinto(i, j)):
            return 0
        if (not self.isDentroLabirinto(i + 1, j) or self.maze.get((i + 1, j), 0)):
            n -= 1
        if (not self.isDentroLabirinto(i - 1, j) or self.maze.get((i - 1, j), 0)):
            n -= 1
        if (not self.isDentroLabirinto(i, j - 1) or self.maze.get((i, j - 1), 0)):
            n -= 1
        if (not self.isDentroLabirinto(i, j + 1) or self.maze.get((i , j + 1), 0)):
            n -= 1
                
        return n




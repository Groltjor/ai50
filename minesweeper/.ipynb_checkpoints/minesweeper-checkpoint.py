import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines



class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
    
        if len(self.cells) == self.count and self.count > 0:
            return set(self.cells)

        return set()

        

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count == 0:
            return set(self.cells)

        return set()

        


    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1


    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Contador de movimientos

        self.contador = 0
        self.movimiento_listo = False

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """

        self.moves_made.add(cell)
        self.mark_safe(cell)

        paquete_celdas = set()
        i = cell[0]
        j = cell[1]

        for fila in range( i -1, i + 2):
            for columna in range( j -1, j + 2):
                if (fila, columna) == cell:
                    continue
                if 0 <= fila < self.height and 0 <= columna < self.width: 
                    coord = (fila, columna)
                    if coord in self.mines:
                        count -= 1
                    if coord not in self.safes and coord not in self.moves_made and coord not in self.mines:
                        paquete_celdas.add(coord)
        
        if paquete_celdas:
            self.knowledge.append(Sentence(paquete_celdas, count))

        cambio = True
        while cambio == True:         
            cambio = False


            for sentence in self.knowledge:
                mines = sentence.known_mines()
                safes = sentence.known_safes()

                for celda in mines:
                    if celda not in self.mines:
                        self.mark_mine(celda)
                        cambio = True

                for celda in safes:
                    if celda not in self.safes:
                        self.mark_safe(celda)
                        cambio = True
            
                    
            if len(self.knowledge) >= 2:
                reglas_nuevas = []
                for s1 in self.knowledge:
                    for s2 in self.knowledge:
                        if s1 != s2 and s1.cells and s2.cells:
                            if s2.cells.issubset(s1.cells):
                                celdas_nuevas = s1.cells - s2.cells
                                count_nuevo = s1.count - s2.count
                                if celdas_nuevas and 0 <= count_nuevo <= len(celdas_nuevas):
                                    sentencia_nueva = Sentence(celdas_nuevas, count_nuevo)
                                    if sentencia_nueva not in self.knowledge and sentencia_nueva not in reglas_nuevas:
                                        reglas_nuevas.append(sentencia_nueva)
    
    
                for regla in reglas_nuevas:
                    self.knowledge.append(regla)
                    cambio = True
                    
                
            
        self.knowledge = [s for s in self.knowledge if s.cells]
        


    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """

        for cell in self.safes:
            if cell not in self.moves_made:
                print("Movimientos Seguro: ", cell)
                return cell
        print("Returnig None")
        return None


    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        x = 0
        size = self.height * self.width
        
        while x < size:
            coordenada_random = (random.randint(0, self.height -1), random.randint(0, self.width -1))
            a, b = coordenada_random
            if (a, b) in self.moves_made or (a, b) in self.mines:
        
                x += 1
                continue
            print("Movimiento Random: ", coordenada_random)
            return (a, b)
                

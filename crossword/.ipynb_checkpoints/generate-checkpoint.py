import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        from pprint import pprint
                
        palabras_validas = {}
        
        for variable, candidatos in self.domains.items():
            palabras_validas[variable] = set()
            
            for palabra in candidatos :
                if len(palabra) == variable.length:
                    palabras_validas[variable].add(palabra)

        self.domains = palabras_validas        

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """        
        
        from pprint import pprint
        overlap = self.crossword.overlaps.get((x,y))
        if overlap is None:
            return False

        i, j = overlap
        palabras_existen = set()
        state = False
        pprint(self.domains[x])
        for palabra_x in self.domains[x]:
            letra_palabra_x = palabra_x[i]
            pprint(self.domains[y])
            for palabra_y in self.domains[y]:
                letra_palabra_y = palabra_y[j]
                if letra_palabra_x == letra_palabra_y:
                    palabras_existen.add(palabra_x) ##  yo opte por crear un diccionario nuevo y después igualarlo, sin embargo tambien se puede eliminar from X.domain
            

        if palabras_existen != self.domains[x]:
            self.domains[x] = palabras_existen
            return True
                            
                            
        return False
                        
                

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """

        from collections import deque


        arcos = {}
        queue = deque()

        if arcs is None:
            for (x, y), overlap in self.crossword.overlaps.items():
                if overlap:
                    arcos[(x, y)] = overlap
                    queue.append((x, y))
        else:
            queue.extend(arcs)
        


        while len(queue) != 0:
            value_x, value_y = queue[0]
            queue.popleft()
            if value_x not in self.domains or value_y not in self.domains:
                continue
            if self.revise(value_x, value_y):
                if len(self.domains[value_x]) == 0:
                    return False
                else:
                    vecinosX = self.crossword.neighbors(value_x)
                    for variableZ in vecinosX:
                        if variableZ == value_y:  ## Revisar
                            continue
                        else:
                            queue.append( (variableZ, value_x) )


        return True

        
            
            
        

        
                
        

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        
        for variable in self.crossword.variables:
            
            if variable not in assignment:
                
                return False
        return True
            

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        from pprint import pprint
        
        for variable, datos in assignment.items():
            if len(datos) != variable.length:
                return False
            else:
                vecinos_datos = self.crossword.neighbors(variable)
                for vecino in vecinos_datos:
                    if vecino in assignment:
                        i, j = self.crossword.overlaps[(variable, vecino)]
                        if datos[i] != assignment[vecino][j]:
                            return False
            if list(assignment.values()).count(datos) > 1:
                return False
        return True
                    
                

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        dominioNuevo_x = {}
        from pprint import pprint

        if len(self.domains[var]) ==1:
            return list(self.domains[var])
        print("Genial, más de un resultadoc")
        if len(self.domains[var]) > 1: ## 
            print("Significa que tiene mas de una palabra asignada todavia a jijo!")
            print("Son:")
            pprint(self.domains[var])
            for palabra in self.domains[var]:
                print("Entramos a loopear en cada palabra")
                if palabra in assignment.values():
                    print("Palabra ya asignada ", palabra)
                    continue
                else:
                    ## Aqui viene lo pesado verdad? revisar como afecta a los vecinos ai dios
                    vecinos_datos = self.crossword.neighbors(var)
                    n = 0
                    for vecino in vecinos_datos:
                        if vecino not in assignment:  ## aquí no me suena

                            if (var, vecino) not in self.crossword.overlaps:
                                continue

                            
                            i, j = self.crossword.overlaps[ (var, vecino) ]
                            for palabra_vecino in self.domains[vecino]:
                                if palabra[i] != palabra_vecino[j]: ## posiblemente tiene problemas con más casos, ya que revisa solo assignment! no se!
                                    print("Si coincide es buena la propuesta, bueno ggg")
                                    n += 1
                dominioNuevo_x[palabra] = n
            
         
        ordenado = sorted(dominioNuevo_x.items(), key = lambda x: x[1])

        listado_final = [palabra for palabra, _ in ordenado]
        print("Final de order_domain", listado_final)
        return listado_final
            
            

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        import math
        mejor_variable = None
        menor_dominio = float("inf")
        mayor_grado = -1

        
        for variable in self.crossword.variables:
            if variable not in assignment:
                dominio = len(self.domains[variable])  ## Esto nos habla del len de palabras
                grado = len(self.crossword.neighbors(variable)) ## Esto nos habla de cuantas afecta

                if dominio < menor_dominio:
                    menor_dominio = dominio
                    mayor_grado = grado
                    mejor_variable = variable

                elif dominio == menor_dominio: ## Si encuentra un caso donde el dominio sea un empate

                    if grado > mayor_grado:
                        mayor_grado = grado
                        mejor_variable = variable

        print("Mejor variable", mejor_variable)
        return mejor_variable
                    
                                         
                
                
                

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        from pprint import pprint

        if len(self.crossword.variables) == len(assignment) and self.consistent(assignment):
            return assignment
        else:
            var = self.select_unassigned_variable(assignment)
            print("No esta asignada!!! Pero la encontramos")
            values = self.order_domain_values(var, assignment)
            if not values:
                print("No hay valores posibles para esta variable:", var)
                return None
            pprint(values)
            for value in values:
                assignment[var] = value
                if self.consistent(assignment):
                    print("SI es consistente")
                    print("Nuestro assignment es: ")
                    pprint(assignment)
                    result = self.backtrack(assignment)
                    if result is not None: ## una forma de expresar no es failure como en el AI50
                        return result
                else:
                    print("No fue consistente con: ", value)
                del assignment[var]

            return None
                
                        
        


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()

"""
Tic Tac Toe
"""
import numpy as np

class TicTacToe():

    def __init__(self, player_symbol):
        # initialize the list of symbols
        self.symbol_list = []
        # defines all nine symbols; all start off as blank  
        for i in range(9):
            self.symbol_list.append("-") 

        # self.player_symbol = player_symbol
     
        if player_symbol == "X":
            self.player_symbol = f"\033[91m{player_symbol}\033[0m" 
        else:
            self.player_symbol = f"\033[94m{player_symbol}\033[0m"
            
    def ocupado(self, grid_coord):
    
        if grid_coord[0].isdigit():
            grid_coord = grid_coord[1] + grid_coord[0]

        col = grid_coord[0].capitalize()
        row = grid_coord[1]

        grid_index = 0
        contrario = ""
        if row == "1":
            if col == "A":
                grid_index = 0
            elif col == "B":
                grid_index = 1
            elif col == "C":
                grid_index = 2
        elif row == "2":
            if col == "A":
                grid_index = 3
            elif col == "B":
                grid_index = 4
            elif col == "C":
                grid_index = 5
        elif row == "3":
            if col == "A":
                grid_index = 6
            elif col == "B":
                grid_index = 7
            elif col == "C":
                grid_index = 8
            
        if self.player_symbol == "X":
            contrario = f"\033[91mO\033[0m"
        else:
            contrario = f"\033[91mX\033[0m"

        return self.symbol_list[grid_index] not in  ["↑", "-", "↓", "→", "←"] or self.symbol_list[grid_index] == contrario

    def restart(self):
        # clears the grid 
        for i in range(9):
            self.symbol_list[i] = "-"

    def colorear(self, color2):
        if color2 == "red":
            color = "\033[91m"
        elif color2 == "blue":
            color = "\033[94m"
        reset_color = "\033[0m"
        print(f"\n       A   B   C\n")
        row_one = f"   1   {self.symbol_list[0]} {color}║{reset_color} {self.symbol_list[1]} {color}║{reset_color} {self.symbol_list[2]}"
        row_two = f"   2   {self.symbol_list[3]} {color}║{reset_color} {self.symbol_list[4]} {color}║{reset_color} {self.symbol_list[5]}"
        row_three = f"   3   {self.symbol_list[6]} {color}║{reset_color} {self.symbol_list[7]} {color}║{reset_color} {self.symbol_list[8]}"

        horizontal_line = f"      {color}═══╬═══╬═══{reset_color}"

        print(row_one)
        print(horizontal_line)
        print(row_two)
        print(horizontal_line)
        print(row_three, "\n")


    def draw_grid(self):
        color = ""
        # display the column headers

        print("\n       A   B   C\n")
        
        # display first row 
        row_one = "   1   " + color + self.symbol_list[0]
        row_one += " ║ " + self.symbol_list[1]
        row_one += " ║ " + self.symbol_list[2]
        print(row_one)

        # display divider
        print("      ═══╬═══╬═══")

        # display second row 
        row_two = "   2   " + self.symbol_list[3]
        row_two += " ║ " + self.symbol_list[4]
        row_two += " ║ " + self.symbol_list[5]
        print(row_two)

        # display divider
        print("      ═══╬═══╬═══")

        # display third and last row 
        row_three = "   3   " + self.symbol_list[6]
        row_three += " ║ " + self.symbol_list[7]
        row_three += " ║ " + self.symbol_list[8]
        print(row_three, "\n")


    def edit_square(self, grid_coord):
        # swamps coordinates such as "1A" to "A1"
        
        if grid_coord[0].isdigit():
            grid_coord = grid_coord[1] + grid_coord[0]

        # divides the coordinate 
        col = grid_coord[0].capitalize()
        row = grid_coord[1]

        # converts "A1" to 0, "C3" to 8, and so forth 
        grid_index = 0

        if row == "1":
            if col == "A":
                grid_index = 0
            elif col == "B":
                grid_index = 1
            elif col == "C":
                grid_index = 2
        elif row == "2":
            if col == "A":
                grid_index = 3
            elif col == "B":
                grid_index = 4
            elif col == "C":
                grid_index = 5
        elif row == "3":
            if col == "A":
                grid_index = 6
            elif col == "B":
                grid_index = 7
            elif col == "C":
                grid_index = 8

        if self.symbol_list[grid_index] in  ["↑", "-", "↓", "→", "←"]:
            self.symbol_list[grid_index] = self.player_symbol


    def update_symbol_list(self, new_symbol_list):
        for i in range(9):
            self.symbol_list[i] = new_symbol_list[i]


    def did_win(self, player_symbol, tipo, counter_x, counter_o):
        # Local variable to replace unwieldy self.symbol_list
        g = []
        for i in range(9):
            g.append(self.symbol_list[i])
        ganador_x = False
        ganador_o = False
        # Get the ANSI color codes for the player's symbols
        x_color = f"\033[91m{player_symbol}\033[0m"
        o_color = f"\033[94m{player_symbol}\033[0m"
        # Check top row
        if g[0] == x_color and g[1] == x_color and g[2] == x_color:
            ganador_x = True

        # Check middle row
        elif g[3] == x_color and g[4] == x_color and g[5] == x_color:
            ganador_x = True

        # Check bottom row
        elif g[6] == x_color and g[7] == x_color and g[8] == x_color:
            ganador_x = True

        # Check left column
        elif g[0] == x_color and g[3] == x_color and g[6] == x_color:
            ganador_x = True

        # Check middle column
        elif g[1] == x_color and g[4] == x_color and g[7] == x_color:
            ganador_x = True

        # Check right column
        elif g[2] == x_color and g[5] == x_color and g[8] == x_color:
            ganador_x = True

        # Check top-right to bottom-left
        elif g[2] == x_color and g[4] == x_color and g[6] == x_color:
            ganador_x = True

        # Check top-left to bottom-right
        elif g[0] == x_color and g[4] == x_color and g[8] == x_color:
            ganador_x = True
            
        elif g[3] == o_color and g[4] == o_color and g[5] == o_color:
            ganador_o = True

        # Check bottom row
        elif g[6] == o_color and g[7] == o_color and g[8] == o_color:
            ganador_o = True

        # Check left column
        elif g[0] == o_color and g[3] == o_color and g[6] == o_color:
            ganador_o = True

        # Check middle column
        elif g[1] == o_color and g[4] == o_color and g[7] == o_color:
            ganador_o = True

        # Check right column
        elif g[2] == o_color and g[5] == o_color and g[8] == o_color:
            ganador_o = True

        # Check top-right to bottom-left
        elif g[2] == o_color and g[4] == o_color and g[6] == o_color:
            ganador_o = True

        # Check top-left to bottom-right
        elif g[0] == o_color and g[4] == o_color and g[8] == o_color:
            ganador_o = True
        # agregue esto ultimo
        elif g[0] == o_color and g[1] == o_color and g[2] == o_color:
            ganador_o = True

        if tipo == 'BO1':           
            if counter_o == 1:
                return "azul"
            if counter_x == 1:
                return "rojo"
        elif tipo == 'BO3':
            if counter_o == 2:
                return "azul"      
            if counter_x == 2:
                return "rojo"   
        elif tipo == 'BO5':
            if counter_o == 3:
                return "azul"
            if counter_x == 3:
                return "rojo"
        if ganador_x == True:
            return "continue"
        elif ganador_o == True:
            return "continue"
        
        return False

    def is_draw(self):
        # see if all the spaces are used up 
        num_blanks = 0
        for i in range(9):
                if self.symbol_list[i] == " " or self.symbol_list[i] in ["↑", "-", "↓", "→", "←"]:
                    num_blanks += 1

        # if the player didn't win and no spaces are left, it's a draw
        if self.did_win(self.player_symbol, ".", 0, 0) == False and num_blanks == 0:
            return True
        else:
            return False
    
    def swap_position(self, player_symbol, coord):
        print("Selected", coord)
        g = []
        for i in range(9):
            g.append(self.symbol_list[i])
        col = coord[0].capitalize()
        row = coord[1]
        while True:
            valid_options = []

            if row == "1":
                if col == "A":
                    if not self.ocupado("B1"):
                        print("1. Mover a B1")
                        valid_options.append("B1")
                    if not self.ocupado("A2"):
                        print("2. Mover a A2")
                        valid_options.append("A2")
                elif col == "B":
                    if not self.ocupado("A1"):
                        print("1. Mover a A1")
                        valid_options.append("A1")
                    if not self.ocupado("C1"):
                        print("2. Mover a C1")
                        valid_options.append("C1")
                    if not self.ocupado("B2"):
                        print("3. Mover a B2")
                        valid_options.append("B2")
                elif col == "C":
                    if not self.ocupado("B1"):
                        print("1. Mover a B1")
                        valid_options.append("B1")
                    if not self.ocupado("C2"):
                        print("2. Mover a C2")
                        valid_options.append("C2")
            elif row == "2":
                if col == "A":
                    if not self.ocupado("A1"):
                        print("1. Mover a A1")
                        valid_options.append("A1")
                    if not self.ocupado("A3"):
                        print("2. Mover a A3")
                        valid_options.append("A3")
                    if not self.ocupado("B2"):
                        print("3. Mover a B2")
                        valid_options.append("B2")
                elif col == "B":
                    if not self.ocupado("A2"):
                        print("1. Mover a A2")
                        valid_options.append("A2")
                    if not self.ocupado("C2"):
                        print("2. Mover a C2")
                        valid_options.append("C2")
                    if not self.ocupado("B1"):
                        print("3. Mover a B1")
                        valid_options.append("B1")
                    if not self.ocupado("B3"):
                        print("4. Mover a B3")
                        valid_options.append("B3")
                elif col == "C":
                    if not self.ocupado("C1"):
                        print("1. Mover a C1")
                        valid_options.append("C1")
                    if not self.ocupado("C3"):
                        print("2. Mover a C3")
                        valid_options.append("C3")
                    if not self.ocupado("B2"):
                        print("3. Mover a B2")
                        valid_options.append("B2")
            elif row == "3":
                if col == "A":
                    if not self.ocupado("A2"):
                        print("1. Mover a A2")
                        valid_options.append("A2")
                    if not self.ocupado("B3"):
                        print("4. Mover a B3")
                        valid_options.append("B3")
                elif col == "B":
                    if not self.ocupado("A3"):
                        print("1. Mover a A3")
                        valid_options.append("A3")
                    if not self.ocupado("C3"):
                        print("2. Mover a C3")
                        valid_options.append("C3")
                    if not self.ocupado("B2"):
                        print("3. Mover a B2")
                        valid_options.append("B2")
                elif col == "C":
                    if not self.ocupado("C2"):
                        print("2. Mover a C2")
                        valid_options.append("C2")
                    if not self.ocupado("B3"):
                        print("4. Mover a B3")
                        valid_options.append("B3")

            if not valid_options:
                return False
            while True:          
                option_swaped = input(f"Enter option: ").upper()
                if option_swaped in valid_options:
                    break
            if option_swaped in valid_options:
                self.edit_square(option_swaped)
                self.delete_coord(coord, option_swaped)
                break
            else:
                print("Opción inválida. Las opciones válidas son:", ", ".join(valid_options))
            
        return True



    def delete_coord(self, grid_coord, option_swaped):
        arriba = "↑"
        abajo = "↓"
        derecha = "→"
        izquierda = "←"
        if grid_coord[0].isdigit():
            grid_coord = grid_coord[1] + grid_coord[0]

        # divides the coordinate
        col = grid_coord[0].capitalize()
        row = grid_coord[1]
        col2 = option_swaped[0].capitalize()
        row2 = option_swaped[1]
        for i in range(9):
            if self.symbol_list[i] in ["↑", "-", "↓", "→", "←"]:
                self.symbol_list[i] = "-"

        # converts "A1" to 0, "C3" to 8, and so forth
        grid_index = 0

        if row == "1":
            if col == "A":
                grid_index = 0
            elif col == "B":
                grid_index = 1
            elif col == "C":
                grid_index = 2
        elif row == "2":
            if col == "A":
                grid_index = 3
            elif col == "B":
                grid_index = 4
            elif col == "C":
                grid_index = 5
        elif row == "3":
            if col == "A":
                grid_index = 6
            elif col == "B":
                grid_index = 7
            elif col == "C":
                grid_index = 8

        if row2 == "1":
            if col2 == "A":
                grid_index2 = 0
            elif col2 == "B":
                grid_index2 = 1
            elif col2 == "C":
                grid_index2 = 2
        elif row2 == "2":
            if col2 == "A":
                grid_index2 = 3
            elif col2 == "B":
                grid_index2 = 4
            elif col2 == "C":
                grid_index2 = 5
        elif row2 == "3":
            if col2 == "A":
                grid_index2 = 6
            elif col2 == "B":
                grid_index2 = 7
            elif col2 == "C":
                grid_index2 = 8
        print(str(grid_index) +" "+str(grid_index2))
        if grid_index+3==grid_index2:
            movement = abajo
        elif grid_index-3==grid_index2:
            movement = arriba
        elif grid_index+1==grid_index2:
            movement = derecha
        elif grid_index-1==grid_index2:
            movement = izquierda
        self.symbol_list[grid_index] = str(movement)

    def ocupado_rival(self, grid_coord):
        if grid_coord[0].isdigit():
            grid_coord = grid_coord[1] + grid_coord[0]

        col = grid_coord[0].capitalize()
        row = grid_coord[1]

        grid_index = 0
        rival_symbol = "X" if self.player_symbol == "O" else "O"  # Determinar el símbolo del rival

        if row == "1":
            if col == "A":
                grid_index = 0
            elif col == "B":
                grid_index = 1
            elif col == "C":
                grid_index = 2
        elif row == "2":
            if col == "A":
                grid_index = 3
            elif col == "B":
                grid_index = 4
            elif col == "C":
                grid_index = 5
        elif row == "3":
            if col == "A":
                grid_index = 6
            elif col == "B":
                grid_index = 7
            elif col == "C":
                grid_index = 8
        self.symbol_list[grid_index] == rival_symbol
        return self.symbol_list[grid_index]



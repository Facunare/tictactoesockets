"""
Tic Tac Toe
"""

class TicTacToe():

    def __init__(self, player_symbol):
        # initialize the list of symbols
        self.symbol_list = []
        # defines all nine symbols; all start off as blank  
        for i in range(9):
            self.symbol_list.append(" ") 

        # initializes the player symbol
        if player_symbol == "X":
            self.player_symbol = f"\033[91m{player_symbol}\033[0m" 
        else:
            self.player_symbol = f"\033[94m{player_symbol}\033[0m"
        # self.player_symbol = player_symbol
    def ocupado(self, grid_coord):
        if grid_coord[0].isdigit():
            grid_coord = grid_coord[1] + grid_coord[0]

        col = grid_coord[0].capitalize()
        row = grid_coord[1]

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

        return self.symbol_list[grid_index] != " "

    def restart(self):
        # clears the grid 
        for i in range(9):
            self.symbol_list[i] = " "

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

        if self.symbol_list[grid_index] == " ":
            self.symbol_list[grid_index] = self.player_symbol


    def update_symbol_list(self, new_symbol_list):
        for i in range(9):
            self.symbol_list[i] = new_symbol_list[i]


    def did_win(self, player_symbol):
        # Local variable to replace unwieldy self.symbol_list
        g = []
        for i in range(9):
            g.append(self.symbol_list[i])

        # Get the ANSI color codes for the player's symbols
        x_color = f"\033[91m{player_symbol}\033[0m"
        o_color = f"\033[94m{player_symbol}\033[0m"

        # Check top row
        if g[0] == x_color and g[1] == x_color and g[2] == x_color:
            return True

        # Check middle row
        elif g[3] == x_color and g[4] == x_color and g[5] == x_color:
            return True

        # Check bottom row
        elif g[6] == x_color and g[7] == x_color and g[8] == x_color:
            return True

        # Check left column
        elif g[0] == x_color and g[3] == x_color and g[6] == x_color:
            return True

        # Check middle column
        elif g[1] == x_color and g[4] == x_color and g[7] == x_color:
            return True

        # Check right column
        elif g[2] == x_color and g[5] == x_color and g[8] == x_color:
            return True

        # Check top-right to bottom-left
        elif g[2] == x_color and g[4] == x_color and g[6] == x_color:
            return True

        # Check top-left to bottom-right
        elif g[0] == x_color and g[4] == x_color and g[8] == x_color:
            return True
        elif g[3] == o_color and g[4] == o_color and g[5] == o_color:
            return True

        # Check bottom row
        elif g[6] == o_color and g[7] == o_color and g[8] == o_color:
            return True

        # Check left column
        elif g[0] == o_color and g[3] == o_color and g[6] == o_color:
            return True

        # Check middle column
        elif g[1] == o_color and g[4] == o_color and g[7] == o_color:
            return True

        # Check right column
        elif g[2] == o_color and g[5] == o_color and g[8] == o_color:
            return True

        # Check top-right to bottom-left
        elif g[2] == o_color and g[4] == o_color and g[6] == o_color:
            return True

        # Check top-left to bottom-right
        elif g[0] == o_color and g[4] == o_color and g[8] == o_color:
            return True


        # Didn't win
        return False

    def is_draw(self):
        # see if all the spaces are used up 
        num_blanks = 0
        for i in range(9):
                if self.symbol_list[i] == " ":
                    num_blanks += 1

        # if the player didn't win and no spaces are left, it's a draw
        if self.did_win(self.player_symbol) == False and num_blanks == 0:
            return True
        else:
            return False

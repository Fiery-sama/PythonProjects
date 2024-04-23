# importing the required modules
import random           # importing the random module
from tkinter import *   # importing everything from tkinter

# defining the main class for the application
class GameApplication(Frame):
    # creating a constructor
    def __init__(self):
        # calling the Frame constructor
        Frame.__init__(self)
        
        # calling the grid() method
        self.grid()
        
        # setting the title of the application
        self.master.title("2048 Game - JAVATPOINT")

        # creating a main frame and setting its background color, border, width, and height
        self.main_frame = Frame(
            self, bg = GameApplication.grid_color, bd = 3, width = 600, height = 600
        )
        # calling the grid() method to structure the frame
        self.main_frame.grid(pady = (120, 0))
 
        # calling the app_GUI() and start() methods
        self.app_GUI()
        self.start()
 
        # binding the keys to the their respective methods
        self.master.bind("<Left>", self.left_key)
        self.master.bind("<Right>", self.right_key)
        self.master.bind("<Up>", self.up_key)
        self.master.bind("<Down>", self.down_key)
 
        # calling the mainloop() method
        self.mainloop()

    # ------------ color chart ------------

    # color of grid
    grid_color = "#bbb0a9"
    # color of empty cells
    emptyCell_color = "#ffd1ae"
    # message background color - WINNER
    winner_bg_color = "#ffcd06"
    # message background color - LOSER
    loser_bg_color = "#a4958b"
    # font color for game over
    gameOver_fontColor = "#ffffff"

    # colors of the cells
    cell_colors = {
        2: "#fcece1",
        4: "#f4e9cb",
        8: "#efb07c",
        16: "#f49444",
        32: "#ff7357",
        64: "#e54b2d",
        128: "#ece18f",
        256: "#fbe02c",
        512: "#ffda47",
        1024: "#ebb41e",
        2048: "#fbd84c"    
    }

    # colors of the cell numbers
    cellNumber_color = {
        2: "#61544f",
        4: "#61544f",
        8: "#ffffff",
        16: "#ffffff",
        32: "#ffffff",
        64: "#ffffff",
        128: "#ffffff",
        256: "#ffffff",
        512: "#ffffff",
        1024: "#ffffff",
        2048: "#ffffff"
    }

    # ------------ font chart ------------

    # font styles of the score board
    scoreLabel_font = ("Grandview", 20)
    score_font = ("Verdana", 32, "bold")
    # font style for game over
    gameOver_font = ("Verdana", 48, "bold")

    # font styles of cell number
    cellNumber_font = {
        2: ("Verdana", 55, "bold"),
        4: ("Verdana", 55, "bold"),
        8: ("Verdana", 55, "bold"),
        16: ("Verdana", 50, "bold"),
        32: ("Verdana", 50, "bold"),
        64: ("Verdana", 50, "bold"),
        128: ("Verdana", 40, "bold"),
        256: ("Verdana", 40, "bold"),
        512: ("Verdana", 40, "bold"),
        1024: ("Verdana", 30, "bold"),
        2048: ("Verdana", 30, "bold"),
    }

    # defining a method to create the grid
    def app_GUI(self):
        # creating an empty list for cells
        self.cells = []
        # creating a nested loop for 2D structure
        for i in range(4):
            # creating an empty list of rows
            row = []
            for j in range(4):
                # creating a cell frame
                frameCells = Frame(
                    self.main_frame,
                    bg = GameApplication.emptyCell_color,
                    width = 150,
                    height = 150
                )
                # using the grid() method to set the position of the frame in the grid
                frameCells.grid(row = i, column = j, padx = 5, pady = 5)
                # creating a label to display number on the cell
                cellNumber = Label(self.main_frame, bg = GameApplication.emptyCell_color)
                # creating a dictionary containing the cell data
                cellData = {"frame" : frameCells, "number" : cellNumber}
                # using the grid() method to set the position of the cell number in the cell
                cellNumber.grid(row = i, column = j)
                # using the append() method to add the generated row to the list of rows
                row.append(cellData)
            # using the append() method to add the row to the cell
            self.cells.append(row)

        # creating a frame to display the score
        score_frame = Frame(self)
        # using the place() method to set the position of the frame
        score_frame.place(relx = 0.5, y = 60, anchor = "center")
        # creating the labels to display score
        Label(
            score_frame,
            text = "Score:",
            font = GameApplication.scoreLabel_font
        ).grid(row = 0) # using the grid() method to set the position of the label
        self.score_label = Label(score_frame, text = "0", font = GameApplication.score_font)
        # using the grid() method to set the position of the label
        self.score_label.grid(row = 1)

    # defining a method to start the game
    def start(self):
        # creating a matrix of zeros
        self.matrix = [[0] * 4 for _ in range(4)]
 
        # filling two random cells with 2s

        # selecting a row and column randomly
        row = random.randint(0, 3)
        column = random.randint(0, 3)

        # setting the value of the selected cell as 2
        self.matrix[row][column] = 2
        # configuring the color and font style of the cell and the number
        self.cells[row][column]["frame"].configure(bg = GameApplication.cell_colors[2])
        self.cells[row][column]["number"].configure(
            bg = GameApplication.cell_colors[2],
            fg = GameApplication.cellNumber_color[2],
            font = GameApplication.cellNumber_font[2],
            text = "2"
        )

        while(self.matrix[row][column] != 0):
            # selecting a row and column randomly
            row = random.randint(0,3)
            column = random.randint(0,3)
        
        # setting the value of the selected cell as 2
        self.matrix[row][column] = 2
        # configuring the color and font style of the cell and the number
        self.cells[row][column]["frame"].configure(bg = GameApplication.cell_colors[2])
        self.cells[row][column]["number"].configure(
            bg = GameApplication.cell_colors[2],
            fg = GameApplication.cellNumber_color[2],
            font = GameApplication.cellNumber_font[2],
            text = "2"
        )
 
        # setting the initial value of the score as 0
        self.score = 0

    # defining a method to compress the cells of the matrix
    def compress_cells(self):
        # creating a matrix having all cell values as 0
        MatrixOne = [[0] * 4 for _ in range(4)]
        for i in range(4):
            # setting the value of the positionFill variable to 0
            positionFill = 0
            for j in range(4):
                # if any cell of the matrix is not 0, compress the cell of the matrix to left_key poition 
                if self.matrix[i][j] != 0:
                    MatrixOne[i][positionFill] = self.matrix[i][j]
                    positionFill += 1
        # setting matrixOne as the main matrix
        self.matrix = MatrixOne
 
    # defining a method to combine_cells the same numbered cells
    def combine_cells(self):
        # using the nested for-loop
        for i in range(4):
            for j in range(3):
                # if the value at matrix[i][j] is not 0 and equal to value at matrix[i][j + 1],
                # doubling the value at the matrix[i][j] and setting the matrix[i][j+1]'s value to 0.
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self .matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    # updating the score by adding the newly combined value to that of the score
                    self.score += self.matrix[i][j]

    # defining a method to reverse_order the order of each row in the matrix
    def reverse_order(self):
        # creating an empty list
        MatrixOne = []
        # using the nested for-loop
        for i in range(4):
            # appending an empty list to MatrixOne
            MatrixOne.append([])
            for j in range(4):
                # reversing the value and appending to MatrixOne
                MatrixOne[i].append(self.matrix[i][3-j])
        # setting the main matrix equal to MatrixOne
        self.matrix = MatrixOne
 
    # defining a method to flip the matrix over the diagonal
    def transpose_matrix(self):
        # creating a 4x4 matrix having all elements as zeros
        MatrixOne = [[0] * 4 for _ in range(4)]
        # using the nested for-loop
        for i in range(4):
            for j in range(4):
                # setting the value of MatrixOne[i][j] to the matrix[j][i]
                MatrixOne[i][j] = self.matrix[j][i]
        # setting the main matrix equal to MatrixOne
        self.matrix = MatrixOne

    # defining a method to insert a new 2 or 4 numbered tile to an empty cell
    def insert_tile(self):
        # randomly selecting the row and column from the matrix
        row = random.randint(0, 3)
        column = random.randint(0, 3)
        # if the selected cell of the matrix is not 0,
        # randomly selecting the row and column from the matrix
        while(self.matrix[row][column] != 0):
            row = random.randint(0, 3)
            column = random.randint(0, 3)
        # randomly setting 2 or 4 on the selected cell
        self.matrix[row][column] = random.choice([2, 4])

    # defining a method to update the GUI to correspond to the newly manipulated matrix
    def update_GUI(self):
        # using the nested for-loop
        for i in range(4):
            for j in range(4):
                # retrieve the cell value
                cellValue = self.matrix[i][j]
                # checking if the cell value is equals to 0
                # and configuring the cell and font color accordingly
                if cellValue == 0:
                    self.cells[i][j]["frame"].configure(bg = GameApplication.emptyCell_color)
                    self.cells[i][j]["number"].configure(bg = GameApplication.emptyCell_color, text = "")
                else:
                    self.cells[i][j]["frame"].configure(bg = GameApplication.cell_colors[cellValue])
                    self.cells[i][j]["number"].configure(
                        bg = GameApplication.cell_colors[cellValue],
                        fg = GameApplication.cellNumber_color[cellValue],
                        font = GameApplication.cellNumber_font[cellValue],
                        text = str(cellValue)
                    )
        # updating the score
        self.score_label.configure(text = self.score)
        # calling the update_idletasks() method to display the widget immediately
        self.update_idletasks()

    # defining a binding method for Left Arrow Key
    def left_key(self, event):
        '''
        since the methods we defined earlier are specifically for the left position,
        therefore we will follow this order to manipulate the matrix:
        
        compressing the cells --> combining the adjacent same numbered cells --> compressing the cells again --> inserting a new tile
        
        after that, we will update the GUI and check for game over
        '''
        
        # compressing the cells
        self.compress_cells()
        # combining the adjacent same numbered cells
        self.combine_cells()
        # compressing the cells again
        self.compress_cells()
        # inserting a new tile
        self.insert_tile()

        # updating the GUI
        self.update_GUI()
        # checking for game over
        self.gameover()

    # defining a binding method for Right Arrow Key
    def right_key(self, event):
        '''
        We will now follow this order to manipulate the matrix for the right key press:
        
        reversing the order of the matrix --> compressing the cells --> combining the adjacent same numbered cells --> compressing the cells again --> reversing the order again --> inserting a new tile
        
        after that, we will update the GUI and check for game over
        '''
        
        # reversing the order of the matrix
        self.reverse_order()
        # compressing the cells
        self.compress_cells()
        # combining the adjacent same numbered cells
        self.combine_cells()
        # compressing the cells again
        self.compress_cells()
        # reversing the order of the matrix again
        self.reverse_order()
        # inserting a new tile
        self.insert_tile()

        # updating the GUI
        self.update_GUI()
        # checking for game over
        self.gameover()
 
    # defining a binding method for Up Arrow Key
    def up_key(self, event):
        '''
        We will now follow this order to manipulate the matrix for the right key press:
        
        flipping the matrix at its diagonal --> compressing the cells --> combining the adjacent same numbered cells --> compressing the cells again --> flipping the matrix at its diagonal again --> inserting a new tile
        
        after that, we will update the GUI and check for game over
        '''

        # flipping the matrix at its diagonal
        self.transpose_matrix()
        # compressing the cells
        self.compress_cells()
        # combining the adjacent same numbered cells
        self.combine_cells()
        # compressing the cells again
        self.compress_cells()
        # flipping the matrix at its diagonal again
        self.transpose_matrix()
        # inserting a new tile
        self.insert_tile()

        # updating the GUI
        self.update_GUI()
        # checking for game over
        self.gameover()
 
    # defining a binding method for Down Arrow Key
    def down_key(self, event):
        '''
        We will now follow this order to manipulate the matrix for the right key press:
        
        flipping the matrix at its diagonal --> reversing the order of the matrix --> compressing the cells --> combining the adjacent same numbered cells --> compressing the cells again --> reversing the order again --> flipping the matrix at its diagonal again --> inserting a new tile
        
        after that, we will update the GUI and check for game over
        '''

        # flipping the matrix at its diagonal        
        self.transpose_matrix()
        # reversing the order of the matrix
        self.reverse_order()
        # compressing the cells
        self.compress_cells()
        # combining the adjacent same numbered cells
        self.combine_cells()
        # compressing the cells again
        self.compress_cells()
        # reversing the order of the matrix again
        self.reverse_order()
        # flipping the matrix at its diagonal again
        self.transpose_matrix()
        # inserting a new tile
        self.insert_tile()

        # updating the GUI
        self.update_GUI()
        # checking for game over
        self.gameover()

    # defining a method to check if any horizontal move exists
    def horizontal_move_exists(self):
        # using the nested for-loop
        for i in range(4):
            for j in range(3):
                # if two horizontally adjacent tiles are same, returning True; else return false 
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False

    # defining a method to check if any vertical move exists
    def vertical_move_exists(self):
        # using the nested for-loop
        for i in range(3):
            for j in range(4):
                # if two vertically adjacent tiles are same, returning True; else return false 
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False
    
    # defining a method to check game over
    def gameover(self):
        # if any tile of the matrix is 2048; then return a label displaying "YOU WIN!!" message
        if any(2048 in row for row in self.matrix):
            # creating a frame
            gameOver_frame = Frame(self.main_frame, borderwidth = 2)
            # placing the frame on the window using the place() method
            gameOver_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
            # creating a label and placing it in the frame
            Label(
                gameOver_frame,
                text = "YOU WIN!!",
                bg = GameApplication.winner_bg_color,
                fg = GameApplication.gameOver_fontColor,
                font = GameApplication.gameOver_font
            ).pack()
        # if there does not exist any horizontal and vertical moves in the game; then return a label displaying "GAME OVER!!" message
        elif not any(0 in row for row in self. matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            # creating a frame
            gameOver_frame = Frame(self.main_frame, borderwidth = 2)
            # placing the frame on the window using the place() method
            gameOver_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
            # creating a label and placing it in the frame
            Label(
                gameOver_frame,
                text = "GAME OVER!!",
                bg = GameApplication.loser_bg_color,
                fg = GameApplication.gameOver_fontColor,
                font = GameApplication.gameOver_font
            ).pack()

# defining a function to run the game
def game():
    # calling the GameApplication() class
    GameApplication()
        
# main function
if __name__ == "__main__":
    # calling the game() function
    game()
    
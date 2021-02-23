from enum import IntEnum
import sys
import random

class TicTacToe:
    # IntEnum makes it easier to access values rather than normal Enum
    class STATES(IntEnum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4

    # Define a var to hold our current state
    GAME_STATE = 0
    # "If my calculations are correct, when this baby hits 0... you're gonna see some serious shit." -Dr. Emmett Brown, probably
    SPACES_LEFT = 9

    # Takes care of drawing the grid and placed markers
    def draw_board(self):
        board = self.board

        print("\n=====\n")
        # Draw board
        for i in board:
            for c in board[i]:
                if list(board[i].keys()).index(c) == 2:
                    print(board[i][c])
                else:
                    print(board[i][c], end='|')
            if list(board.keys()).index(i) < 2:
                print('-+-+-')

        if self.GAME_STATE == self.STATES.CROSS_TURN:
            print("\nIt is X's turn!")
        else:
            print("\nIt is O's turn!")
        
        #print(board[1][1] + '|' + board[1][2] + '|' + board[1][3])
        #print('-+-+-')
        #print(board[2][1] + '|' + board[2][2] + '|' + board[2][3])
        #print('-+-+-')
        #print(board[3][1] + '|' + board[3][2] + '|' + board[3][3])

    # Init
    def __init__(self):
        print('Starting Tic-Tac-Toe...')
        self.GAME_STATE = round(random.uniform(0, 1), 0)
        self.board = {1: {1: ' ', 2: ' ', 3: ' '},
                      2: {1: ' ', 2: ' ', 3: ' '},
                      3: {1: ' ', 2: ' ', 3: ' '}
                      }
        self.draw_board()

    # Best kind of checks are if statements, no one uses paper anymore...
    def check_for_win(self):
        # Horizontal
        if (self.board[1][1] == self.board[1][2] == self.board[1][3] != ' ' or
            self.board[2][1] == self.board[2][2] == self.board[2][3] != ' ' or
            self.board[3][1] == self.board[3][2] == self.board[3][3] != ' '):
            pass
        # Vertical
        elif (self.board[1][1] == self.board[2][1] == self.board[3][1] != ' ' or
              self.board[1][2] == self.board[2][2] == self.board[3][2] != ' ' or
              self.board[1][3] == self.board[2][3] == self.board[3][3] != ' '):
            pass
        # Diag
        elif (self.board[1][1] == self.board[2][2] == self.board[3][3] != ' ' or
              self.board[1][3] == self.board[2][2] == self.board[3][1] != ' '):
            pass
        else:
            # Needs to be after all other calls to prevent accidently calling a last move win a draw
            if self.SPACES_LEFT == 0:
                self.draw_board()
                self.GAME_STATE = self.STATES.DRAW
                print("DRAW!")
                sys.exit(1)
            return False
        
        print("WINNER WINNER CHICKEN DINNER!")
        if self.GAME_STATE == self.STATES.CROSS_TURN:
            self.draw_board()
            self.GAME_STATE = self.STATES.CROSS_WON
            print("X's has WON!")
        else:
            self.draw_board()
            self.GAME_STATE = self.STATES.NAUGHT_WON
            print("O's has WON!")
        sys.exit(0)
        
    def place_marker(self, symbol, row, column):
        # Covnert input to the format we desire
        # - Capitalize symbol
        # - Interize row and column
        # Ensure we were given valid input
        symbol = symbol.capitalize()
        row = int(row)
        column = int(column)
        if symbol != "X" and symbol != "O":
            print("This is Tic-Tac-Toe! Ya know, with X's and O's! Not X's and " + symbol + "'s...")
            return False
        if row > 3 or column > 3:
            print("Invalid input! You cannot assign a marker to a number outside the grid dummy! Enter numbers between 1 and 3 (inclusive)")
            return False

        # Check that it is actually that symbols turn
        # This if/else could most likely be made simpler but this works
        if (self.GAME_STATE == self.STATES.CROSS_TURN and symbol == 'X') or (self.GAME_STATE == self.STATES.NAUGHT_TURN and symbol == 'O'):
            pass
        else:
            print("Hey! It's not your turn!")
            self.draw_board()
            return False

        # Check coordinate for existing occupancy
        if self.board[row][column] != ' ':
            print('Spot already occupied! Are you trying to cheat?')
            self.draw_board()
            return False
        
        # Set the requested symbol at the requested coordinate 
        self.board[row][column] = symbol
        self.SPACES_LEFT -= 1
        
        self.check_for_win()
        
        # Update who's turn it is
        if self.GAME_STATE == self.STATES.CROSS_TURN:
            self.GAME_STATE = self.STATES.NAUGHT_TURN
        else:
            self.GAME_STATE = self.STATES.CROSS_TURN

        # Redraw the board
        self.draw_board()
        return True

    # Prompt for input for faster playing
    def play(self):
        while (self.GAME_STATE < 2):
            row = input("Row: ")
            # Secret double input... sssshhhhhhh
            if len(row) == 2:
                source = row
                row = source[0]
                column = source[1]
            else:
                column = input("Column: ")
                
            if self.GAME_STATE == self.STATES.CROSS_TURN:
                self.place_marker("X", row, column)
            else:
                self.place_marker("O", row, column)

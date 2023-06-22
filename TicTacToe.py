
board = []


def initialize_board() -> list:
    global board
    board = [[' '*3]*3]


def cls() -> None:
    '''clears the screen'''
    print ("\n" * 100)


def display(board: list) -> None:
    '''display the gameboard'''
    cls()
    for row in board:
        print(row)


def get_user_move()-> list:
    '''gets the next move from the user'''


def show_menu():
    '''display the menu'''
    cls()
    print("Hi there, welcome to my Tic-Tac-Toe game!")
    print("1 - Start playing")
    print("2 - Exit")

def get_user_choice() -> int:
    '''get the user choice from the menu'''
    valid =  [1,2]
    choice = -1
    while choice not in valid:
        
        choice = input('Please enter your choice: ')
               






if __name__  == 'main':

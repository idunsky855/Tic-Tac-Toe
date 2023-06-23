

def initialize_board():
    '''init empty gameboard'''
    board = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]
    return board


def cls():
    '''clears the screen'''
    print ("\n" * 100)


def display(board: list):
    '''display the gameboard'''
    cls()
    i = 0
    print('    0    1    2')
    for row in board:
        print(i ,row)
        i+=1


def show_menu():
    '''display the menu'''
    cls()
    print("Hi there, welcome to my Tic-Tac-Toe game!")
    print("1 - Start playing")
    print("2 - Exit\n")


def get_user_choice():
    '''get the user choice from the menu'''
    valid =  ['1','2']
    choice = -1
    while choice not in valid:
        
        choice = input('Please enter your choice: ')
        if not choice.isdigit():
            print('Wrong input, please enter either 1 or 2')

    return int(choice)    
    

def play():
    #tic-tac-toe game
    
    board = initialize_board()
   
    while not game_ended:
        display(board)
    

def get_user_move(user_sym: chr ,board: list):
    '''gets the next move from the user '''
    pass


def game_ended(board: list):
    '''checks if the board has a sequence of 3 'x' or 3 'o', returns if someone won and who -> (True,'x') '''
    for i in range(0,3):
        #if all row is 'x' or 'o'
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return (True,board[i][0])
        
        #if all coloumn is 'x' or 'o'
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return (True,board[0][i])

    #first diagonal is 'x' or 'o'
    if board[0][0] == board[1][1]==board[2][2] != ' ':
        return (True,board[1][1])
    
    #second diagonal is 'x' or 'o'
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return (True, board[1][1])
    
    #no sequence of 3 'x' or 3 'o'
    return (False, 0)
    


#main
if __name__ == '__main__':
    game_on = True
    
    while game_on:
        #display menu to user
        show_menu()
    
        #get the user choice 1 - Start playing, 2 - Exit
        user_choice = get_user_choice()
    
        if user_choice == 2:
            game_on = False
        else:
            play()

    #goodbye message
    print("Thanks for playing, Bye!")


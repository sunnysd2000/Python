board=["-","-","-",
       "-","-","-",
       "-","-","-"]
game_continue=True

winner=None

curr_player="X"

def display():
    print(board[0] + " | " + board[1] +" | " + board[2])
    print(board[3] + " | " + board[4] +" | " + board[5])
    print(board[6] + " | " + board[7] +" | " + board[8])

def play_game():
    display()
    
    while game_continue:
        
        give_turn(curr_player)
        
        check_gameover()
        flip_player()
        
    if winner=="X" or winner=="O":
        print(winner + " won. ")
    elif winner==None:
        print("Tie")
            
def give_turn(player):
    print(player + "'s turn.")
    
    pos=input("Enter position from 1 to 9:")
    
    while pos not in ['1','2','3','4','5','6','7','8','9']:
        
        pos=input("Enter position from 1 to 9:")
        
    pos=int(pos)-1
            
    if board[pos]!="-":
        print("Invalid move")
        flip_player()
    else:        
        board[pos]=player
        display()

def check_gameover():
    check_winner()
    check_tie()

def check_winner():
    global winner
    
    row_winner=check_rows()
    
    col_winner=check_columns()
    
    diagonal_winner=check_diagonals()
    
    if row_winner:
        winner=row_winner
    elif col_winner:
        winner=col_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    return

def check_rows():
    
    global game_continue
     
    row1=board[0]==board[1]==board[2]!='-'
    row2=board[3]==board[4]==board[5]!='-'
    row3=board[6]==board[7]==board[8]!='-'
    
    if row1 or row2 or row3:    
        game_continue=False 
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return 

def check_columns():
    
    global game_continue
     
    col1=board[0]==board[3]==board[6]!='-'
    col2=board[1]==board[4]==board[7]!='-'
    col3=board[2]==board[5]==board[8]!='-'
    
    if col1 or col2 or col3:
        game_continue=False 
    if col1:
        return board[0]
    elif col2:
        return board[3]
    elif col3:
        return board[6]
    return 
    
def check_diagonals():
    
    global game_continue
     
    di1=board[0]==board[4]==board[8]!='-'
    di2=board[2]==board[4]==board[6]!='-'
    
    if di1 or di2:
        game_continue=False  
    if di1:
        return board[0]
    elif di2:
        return board[2]
    return   
    
def check_tie():
    global game_continue
    if '-'not in board:
        game_continue=False
    return

def flip_player():
    global curr_player
    
    if curr_player=="X":
        curr_player="O"
    elif curr_player=="O":
        curr_player="X"
    return

play_game()

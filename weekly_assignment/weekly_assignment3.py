class position_not_valid(Exception):
    pass

# function to print the game  board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*(4*len(board)-1))

# function to whether the player won or not
def check_win(board,symbol):
    size=len(board)
    
    # to check for rows
    for i in range(size):
        row_win=True
        for j in range(size):
            if board[i][j]!=symbol:
                row_win=False
                break
        if row_win:
            return True
    
    # to check for columns
    for i in range(size):
        col_win=True
        for j in range(size):
            if board[j][i]!=symbol:
                col_win=False
                break
        if col_win:
            return True
    
    # to check for main diagonal
    main_diag=True
    for i in range(size):
        if board[i][i]!=symbol:
            main_diag=False
            break
    if main_diag:
        return True
    
    # to check for anti diagonal
    anti_diag=True
    for i in range(size):
        if board[i][size-i-1]!=symbol:
            anti_diag=False
            break
    if anti_diag:
        return True
    
    return False

# function to make the move game board
def get_move(board,symbol,player):
    size=len(board)
    dict1={}
    letter=1
    for i in range(size):
        for j in range(size):
            dict1[str(letter)]=(i,j)
            letter+=1

    while True:

        # raising exception for entering invalid position
        try:
            position=input(f"{player}, Enter the position number where you want to enter the symbol(1 to (size*size)): ")

            if not int(position) in range(1,(size*size)+1) or not position.isnumeric():
                raise position_not_valid
            
        except position_not_valid:
            print("invalid number, please enter again")
        else:
            row=dict1[position][0]
            col=dict1[position][1]
            if row < 0 or row>=size or col<0 or col>=size:
                print("Invalid move! Row and Column  must be  within the board: ")
                continue
            if not board[row][col].strip().isnumeric():
                print("Invalid move! That cell is alrady occupied.")
                continue
            board[row][col]=symbol
            break
        


# function for driving the main tic tac toe game
def tic_tac_toe():
    print("Welcome to Tic tac toe game! ")
    player1=input("enter player 1's name: ")
    player2=input("enter player 2's name: ")
    board_size=int(input("Enter the board size: "))
    player1_symbol=input(f"{player1} Enter your symbol(should not be numeric): ")
    player2_symbol=input(f"{player2} Enter your symbol(should not be numeric): ")

    player_symbols={
        player1:player1_symbol,
        player2:player2_symbol
    }

    game_played=0
    wins={
        player1:0,
        player2:0
    }
    draws=0

    while True:
        board=[]
        letter=1
        for i in range(board_size):
            r=[]
            for j in range(board_size):
                r.append(str(letter))
                letter+=1
            board.append(r)

        current_player=player1
        print_board(board)

        for _ in range(board_size**2):
            symbol=player_symbols[current_player]
            get_move(board,symbol,current_player)
            print_board(board)
            if check_win(board,symbol):
                print(f"Congratulation, {current_player} wins!")
                wins[current_player]+=1
                break

            d=True
            for row in board:
                for cell in row:
                    if cell.strip().isnumeric():
                        d=False
                        break
                if not d:
                    break
            
            if d:
                print("Its a draw!")
                draws+=1
                break
            
            if current_player==player1:
                current_player=player2
            else:
                current_player=player1
        
        game_played+=1

        print(f"No of games played: {game_played}")
        print(f"Wins for {player1}: {wins[player1]}")
        print(f"Wins for {player2}:{wins[player2]}")

        play_again=input("Do you want to play again: ").lower()
        if play_again!='yes':
            print("Thanks for playing.")
            break

if __name__=="__main__":
    tic_tac_toe()
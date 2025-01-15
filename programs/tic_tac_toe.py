def create_board():
    return [" " for _ in range(9)]

def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def is_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    
    return False

def is_board_full(board):
    return " " not in board

def is_valid_move(board, position):
    return 0 <= position <= 8 and board[position] == " "

def play_game():
    board = create_board()
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered from 0-8, left to right, top to bottom")
    
    while True:
        display_board(board)
        
        # Get player move
        while True:
            try:
                position = int(input(f"Player {current_player}, enter your move (0-8): "))
                if is_valid_move(board, position):
                    break
                print("Invalid move! Try again.")
            except ValueError:
                print("Please enter a number between 0 and 8!")
        
        # Make move
        board[position] = current_player
        
        # Check win
        if is_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check draw
        if is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

def main():
    while True:
        play_game()
        if input("\nPlay again? (y/n): ").lower() != 'y':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
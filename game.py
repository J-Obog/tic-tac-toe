print("Hello player!") 

def printBoard(board):
    for i in range(0,9,3):
        print(board[i], board[i+1], board[i+2])

def checkWinner(board, turn):
    letter = 'X' if turn == 1 else 'O'
    
    if board[0] == letter and board[1] == letter and board[2] == letter:
        return True

    if board[3] == letter and board[4] == letter and board[5] == letter:
        return True

    if board[6] == letter and board[7] == letter and board[8] == letter:
        return True

    if board[0] == letter and board[3] == letter and board[6] == letter:
        return True
    


def main():
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    
    playerTurn = 1

    while(not checkWinner(board, playerTurn)):
        print(f"Player {playerTurn} turn!")
        printBoard(board)
        spot = int(input("Please pick a spot (1-9)"))
        board[spot - 1] = 'X' if playerTurn == 1 else 'O'
        playerTurn = 2 if playerTurn == 1 else 1

if __name__=="__main__":
  main()

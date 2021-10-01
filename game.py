print("Hello player!") 

def printBoard(board):
    for i in range(0,9,3):
        print(board[i], board[i+1], board[i+2])

def main():
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    
    playerTurn = 1
    playing = True

    while(playing):
        print(f"Player {playerTurn} turn!")
        printBoard(board)
        spot = int(input("Please pick a spot (1-9)"))
        board[spot - 1] = 'X' if playerTurn == 1 else 'O'
        playerTurn = 2 if playerTurn == 1 else 1
        break

if __name__=="__main__":
  main()

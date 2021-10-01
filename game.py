print("Hello player!") 

def printBoard(board):
    for i in range(3):
        print(board[i][0], board[i][1], board[i][2])

def main():
    board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

    printBoard(board)

if __name__=="__main__":
  main()

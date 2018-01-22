import random

def inputPlayerLetter():
    print("Enter a letter. Either X (or) O")
    char = input().upper()
    print("Good, you've entered "+ char)
    if(char == 'X'):
        return ['X']['O']
    else:
        return ['O']['X']

def drawBoard(board):
     print(board[7] + '|' + board[8] + '|' + board[9])
     print('-+-+-')
     print(board[4] + '|' + board[5] + '|' + board[6])
     print('-+-+-')
     print(board[1] + '|' + board[2] + '|' + board[3])


def firstTurnDetermine():
    if(random.randint(0,1) == 0):
        return 'computer'
    else:
        return 'player'

def playerMove():
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def isWinner(bo, le):
      return ((bo[7] == le and bo[8] == le and bo[9] == le) or
      (bo[4] == le and bo[5] == le and bo[6] == le) or
      (bo[1] == le and bo[2] == le and bo[3] == le) or
      (bo[7] == le and bo[4] == le and bo[1] == le) or
      (bo[8] == le and bo[5] == le and bo[2] == le) or
      (bo[9] == le and bo[6] == le and bo[3] == le) or
      (bo[7] == le and bo[5] == le and bo[3] == le) or
      (bo[9] == le and bo[5] == le and bo[1] == le))


def makeMove(board,letter,  move):
    board[move] == letter

def isSpaceFree(board, move):
    return  board[move] == ' '





print('Tic-Tac-Toe Game Begins now!')

while True:
    board = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    firstPlayer = firstTurnDetermine()
    print("The player " + firstPlayer + " will go first.")
    gameOver = False
    while not gameOver:
        if firstPlayer == 'player':
            drawBoard(board)
            move = playerMove(board)









import random

def inputPlayerLetter():
    print("Enter a letter. Either X (or) O")
    char = input().upper()
    print("You've entered "+ char)
    if(char == 'X'):
        return ('X','O')
    else:
        return ('O','X')

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


def makeMove(board, letter, move):
    board[move] = letter

def isSpaceFree(board, move):
    if board[move] == ' ':
        return True
    return False

def isBoardFull(board):
    for i in range(10):
        if(board[i] == ' '):
            return False
    return True

def getBoardCopy(board):
    duplicate_board = []
    for i in range(10):
        duplicate_board.append(i)
    return duplicate_board

def getRandomMove(board, list):

    freeSpaceList = []
    for i in range(10):
        if isSpaceFree(board, i):
            freeSpaceList.append(i)

    if len(freeSpaceList) > 0:
        return random.choice(freeSpaceList)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(10):
        #choose a winning move for computer
        dupBoard = getBoardCopy(board)
        for i in range(10):
            if isSpaceFree(dupBoard, i):
                makeMove(dupBoard, computerLetter, i)
                if isWinner(dupBoard, computerLetter):
                     return i

        #block the winning move of player
        dupBoard = getBoardCopy(board)
        for i in range(10):
            if isSpaceFree(dupBoard,  i):
                makeMove(dupBoard, playerLetter, i)
                if isWinner(board, playerLetter):
                    return i

        #move in corners positions
        possibleMoveList = [1,3,7,9]
        move = getRandomMove(board, possibleMoveList)
        if move!= None:
            return move

        #move in center
        if isSpaceFree(board, 5):
            return 5

        #move at remaining places
        possibleMoveList = [2,4,6,8]
        move = getRandomMove(board, possibleMoveList)
        if( move!= None):
            return move

print('Tic-Tac-Toe Game Begins now!')

while True:
    board = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    currentPlayer = firstTurnDetermine()
    print("The player " + currentPlayer + " will go first.")
    gameOver = False
    while not gameOver:
        if currentPlayer == 'player':
            drawBoard(board)
            move = playerMove()
            makeMove(board, playerLetter , move)
            if isWinner(board, playerLetter) == True:
                drawBoard(board)
                print("Wohoo! You won the game!")
                gameOver = True
            else:
                if isBoardFull(board) == True:
                    drawBoard(board)
                    print('It is a tie!')
                    gameOver = True
                    break
                else:
                    currentPlayer = 'computer'


        if currentPlayer == 'computer':
            print("Computer : Thinking....")
            drawBoard(board)
            print()
            print()
            print()
            move = getComputerMove(board, computerLetter)
            makeMove(board, computerLetter, move)
            if isWinner(board, computerLetter) == True:
                drawBoard(board)
                print("Uh oh! :( You lost the game! Better luck next time.")
                gameOver = True
            else:
                if isBoardFull(board) == True:
                    drawBoard(board)
                    print('It is a tie!')
                    gameOver = True
                    break
                else:
                    currentPlayer = 'player'

    if gameOver:
         exit()








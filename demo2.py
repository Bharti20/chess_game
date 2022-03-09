
# bR ='♜'
# bQ = '♛'
# bK = '♚'
# bKn = '♞'
# bB = '♝'
# bP = '♟'

# wR ='♖'
# wQ = '♕'
# wK = '♔'
# wKn = '♘'
# wB = '♗'
# wP = '♙'

board = [['   ' for i in range(8)] for i in range(8)]
board[0] = ['bbR', 'bbN', 'bbB', 'bbQ', 'bbK', 'bbB', 'bbN', 'bbR']
board[7] = ['wwR', 'wwN', 'wwB', 'wwQ', 'wwK', 'wwB', 'wwN', 'wwR']
x = 1
for i in range(8):
    a = str(x)
    board[1][i] = 'bP'+a
    board[6][i] = 'wP'+a
    x = x+1
def printBoard():
        wall = ""
        for i in range(49):
                wall += "_"
        print(wall)
        for i in range(len(board)):
                s = "|"
                for j in board[i]:
                        if len(j) == 2:
                                s += (" " + str(j) + "|")
                        else:
                                s += (" " + str(j) + " |")
                print(s)
        wall = ""
        for i in range(49):
                wall += "_"
        print(wall)
printBoard()

def pawn_move(start):
    raw = int(input('Enter raw number where you wnat to move  '))
    if start[0] == 'b':
        if raw > 1:
            pos = board[1].index(start) #to 
            to = ' '
            a = board[raw].insert(pos, start)
        else:
            print('Wrong move')
    elif start[0] == 'w':
        if raw < 6:
            pos = board[6].index(start) #to 
            # to = ' '
            # index = raw
            if board[raw][pos] == '   ' or board[raw+1][pos] == '   ':
                
                board[raw].insert(pos, start)
            else:
                print('Can not move')
               
                
        else:
            print('Wrong move')


while True:
        start = input("From: ")
        print(start)
        # to = input("To: ")
        if start[1] == 'P':
            pawn_move(start)
        
        else:
            print('Wrong inpu')

        # if start[0] == 'b':

        # # b = board[1][1] # start
        # # pos = board[1].index('P2') #to
        # # element = board[1].index(start)
        #     pos = board[1].index(to) #to 
        #     print(2)
        #     to = ' '
        #     a = board[3].insert(pos, start)
        # elif start[0] == 'w':
        #     pos = board[6].index(to) #to 
        #     print(2)
        #     # to = ' '
        #     a = board[5].insert(pos, start)

        printBoard()
       












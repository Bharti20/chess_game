"""
In this project i have created chess board usging chess piece's short name like bP1(black pawn)
and created two functions for "PAWN" and "KING" moves. 
"""



board = [['   ' for i in range(8)] for i in range(8)]
board[0] = ['bbR', 'bbN', 'bbB', 'bbQ', 'bbK', 'bbB', 'bbN', 'bbR']   # b - black
board[7] = ['wwR', 'wwN', 'wwB', 'wwQ', 'wwK', 'wwB', 'wwN', 'wwR']  # w - white
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
        z = 0
        for i in range(len(board)):
                s = str(z)
                for j in board[i]:
                        if len(j) == 2:
                                s += (" " + str(j) + "|")
                        else:
                            s += (" " + str(j) + " |")
                print(s)
                z+=1
        wall = ""
        for i in range(49):
                wall += "_"
        print(wall)
printBoard()

def pawn_move(start, raw):
    if start[0] == 'b':    #For the Black pawn move
        z = " "
        if raw > 1:
            for i in range(8):  # This loop for find pawn in board
                if start in board[i]:
                    for j in board[i]:
                        if j == start:
                            start_pos = i
                            break
                    else:
                        z+= 'not found'
            if z != 'not found':
                pos = board[start_pos].index(start) 
                distance = raw - start_pos      # This is for tracking of pawn step
                if board[raw][pos] == '   ' and distance == 1 or distance ==2:
                    board[raw][pos] = start
                    board[start_pos][pos] ='   '
                else:
                    print('can not move')
        else:
            print('Wrong move')
    
    elif start[0] == 'w':   #FOR WHITE PAWN MOVE
        z = " "
        if raw < 6:
            for i in range(8):
                if start in board[i]:
                    for j in board[i]:
                        if j == start:
                            start_pos = i
                            break
                    else:
                        z+= 'not found'
            if z != 'not found':     
                pos = board[start_pos].index(start) #to 
                distance = start_pos-raw  # This is for pawn step tracking
                if board[raw][pos] == '   ' and distance == 1 or distance == 2:
                    board[raw][pos] = start
                    board[start_pos][pos] ='   '
                else:
                    print('Can not move')
        else:
            print('Wrong move')
    else:
        print('Wrong input')

def kingMove(start, raw):
    current_pos = int(input('From (raw no) : '))
    if start[0] == 'b':
        if raw >= 0:
            pos = board[current_pos].index(start) #to
            distance = raw - current_pos   # This is for pawn step tracking
            if board[raw][pos] == '   ' and distance == 1:
                board[raw][pos] = start
                board[current_pos][pos] ='   '
            else:
                print('can not move')
        else:
            print('Wrong move')

    elif start[0] == 'w':
        if raw <= 7:
            pos = board[current_pos].index(start) #to
            distance = current_pos-raw  # This is for tracking of king step
            if board[raw][pos] == '   ' and distance == 1:
                board[raw][pos] = start
                board[current_pos][pos] ='   '
            else:
                print('can not move')
        else:
            print('Wrong move')
    else:
        print('Wrong input')

while True:
    print()
    start = input("From (Enter piece name from board) : ")  #Pieces name are "bbR, wwR, bP1,wP1... '
    print()
    print()
    raw = int(input('To (raw no) '))    
    if start[1] == 'P':
        pawn_move(start, raw)
    elif start[2] == 'K':
        kingMove(start, raw)
    else:
        print('Wrong inpu')

    printBoard()
       












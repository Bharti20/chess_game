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
    if start[0] == 'b':    #For Black pawn move
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
                pos = board[start_pos].index(start) #to
                distance = raw - start_pos   # This is for pawn step tracking
                if board[raw][pos] == '   ' and distance == 1 or distance ==2:
                    board[raw].insert(pos, start)
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
                    board[raw].insert(pos, start)
                    board[start_pos][pos] ='   '
                else:
                    print('Can not move')
        else:
            print('Wrong move')

# def kingMove(start):
#     raw = int(input('Enter raw number where you wnat to move  '))
#     if start[0] == 'b':
#         if raw > 1:
#             pos = board[1].index(start) #to
#             distance = raw - start_pos   # This is for pawn step tracking
#             if board[raw][pos] == '   ' and distance == 1 or distance ==2:
#                 board[raw].insert(pos, start)
#                 board[1][pos] ='   '
#             else:
#                 print('can not move')
    





while True:
    start = input("From: ")
    if start[1] == 'P':
        pawn_move(start)
    
    # elif start[2] == 'K':
    #     kingMove(start)
        
    
    else:
        print('Wrong inpu')

    printBoard()
       












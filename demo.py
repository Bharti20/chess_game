
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
# board = [['  ' for i in range(8)] for i in range(8)]
# board[0] = [bR, bKn, bB, bQ, bK, bB, bKn, bR]
# board[7] = [ wR, wKn, wB, wQ,wK, wB, wKn, wR]

# for i in range(8):
#     board[1][i] = bP
#     board[6][i] = wP

# for i in board:
#         print(*i)






bR ='♜'
bQ = '♛'
bK = '♚'
bKn = '♞'
bB = '♝'
bP = '♟'

wR ='♖'
wQ = '♕'
wK = '♔'
wKn = '♘'
wB = '♗'
wP = '♙'

board_With_Str = [[' ' for i in range(8)] for i in range(8)]



class piece:
    def __init__(self, team, type, image, killable = False):
        self.team = team
        self.type = type 
        self.killable = killable
        self.image = image
    
black_p = piece('b', 'p', bP)
white_p = piece('w', 'p', wP)
black_king = piece('b', 'k', bK)
white_king = piece('w', 'k', wK)
black_rook = piece('b', 'r', bR)
white_rook = piece('w', 'r', wR)
black_bishop = piece('b', 'b', bB)
white_bishop = piece('w', 'b', wB)
black_queen = piece('b', 'bq', bQ)
white_queen = piece('w', 'wq', wQ)
black_knight = piece('b', 'kn', bKn)
white_knight = piece('w', 'kn', wKn)

starting_order = {(0,0):bR, (1,0):bKn, (2,0):bB, (3,0):bK, (4,0):bQ, (5,0):bB, (6,0):bKn, (7,0):bP,
(0,1):bB, (1,1):bB, (2,1):bB,(3,1):bB, (4,1):bB,  (5,1):bB,  (6,1):bB,(7,1):bB,
(0,2):None, (1,2):None, (2,2):None, (3,2):None, (4,2):None, (5,2):None, (6,2):None, (7,2):None,
(0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
(4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
(0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
(4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
(0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
(4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,
(0,6):bB, (1,6):bB, (2,6):bB,(3,6):bB, (4,6):bB,  (5,6):bB,  (6,6):bB,(7,6):bB,
(0,7):wR, (1,7):wKn, (2,7):wB, (3,7):wK, (4,7):wQ, (5,7):wB, (6,7):wKn, (7,7):wB, (7,8):wR, (0,1):wB, (1,1):wB, (2,1):wB,(3,1):wB, (4,1):wB,  (5,1):wB,  (6,1):wB
}
def createBoard(board):
    board[0] = [piece('b', 'r', bR), piece('b', 'kn', bKn), piece('b', 'b', bB), \
                piece('b', 'bq', bQ),piece('b', 'K', bK),piece('b', 'b', bB), \
                piece('b', 'kn', bKn), piece('b', 'r', bR)]
    board[7] = [piece('w', 'r', wR), piece('w', 'kn', wKn), piece('w', 'b', wB),\
                piece('w', 'wq', wQ),piece('w', 'K', wK),piece('w', 'b', wB),\
                piece('w', 'kn', wKn), piece('w', 'r', wR)]

    for i in range(8):
        board[1][i] = piece('b', 'p', bP)
        board[6][i] = piece('w', 'p', wP)
    return board
def printBoard():
        board = createBoard()
        buffer = ""
        for i in range(33):
                buffer += "_"
        print(buffer)
        for i in range(len(board)):
                tmp_str = "|"
        for j in board[i]:
                if len(j) == 2:
                        tmp_str += (" " + str(j) + "|")
                else:
                        tmp_str += (" " + str(j) + " |")
        print(tmp_str)
        buffer = ""
        for i in range(33):
                buffer += "_"
        print(buffer)
printBoard()





# def translate(s):
#     """
#     Translates traditional board coordinates of chess into list indices
#     """
#     try:
#         row = int(s[0])
#         col = s[1]
#         if row < 1 or row > 8:
#             print(s[0] + "is not in the range from 1 - 8")
#             return None
#         if col < 'a' or col > 'h':
#             print(s[1] + "is not in the range from a - h")
#             return None
#         dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
#         return (8 - row, dict[col])
#     except:
#         print(s + "is not in the format '[number][letter]'")
#         return None
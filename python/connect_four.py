
#~~~~~~~~~~~
class Token:
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return "Token({})".format(self.color)

#~~~~~~~~~~~

class Board:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def check_if_filled(self, move, token):
        row = 6
        while row > 0:
            target = str(move) + str(row) # '16'
            if self.coordinates[target] == ' ':
                self.coordinates[target] = token
                break
            else:
                row -= 1

    def __str__(self):
        d = self.coordinates
        row1 = ' | '.join([d['11'], d['21'], d['31'], d['41'], d['51'], d['61'], d['71']])
        row2 = ' | '.join([d['12'], d['22'], d['32'], d['42'], d['52'], d['62'], d['72']])
        row3 = ' | '.join([d['13'], d['23'], d['33'], d['43'], d['53'], d['63'], d['73']])
        row4 = ' | '.join([d['14'], d['24'], d['34'], d['44'], d['54'], d['64'], d['74']])
        row5 = ' | '.join([d['15'], d['25'], d['35'], d['45'], d['55'], d['65'], d['75']])
        row6 = ' | '.join([d['16'], d['26'], d['36'], d['46'], d['56'], d['66'], d['76']])
        return """{}\n-------------------------\n{}\n-------------------------\n{}\n-------------------------\n{}\n-------------------------\n{}\n-------------------------\n{}\n-------------------------
        """.format(row1, row2, row3, row4, row5, row6)

#~~~~~~~~~~~
def read_game_moves_file():
    """
    This helper function reads in the game moves input file 4-moves.txt
    :returns: the games moves input as a list()-->[]
    """
    move_list = []
    with open('4-moves.txt') as moves_file:
        moves = moves_file.readlines()
        [move_list.append(move.strip()) for move in moves]
    return move_list

#~~~~~~~~~~~~~~~~~~~~~
def initialize_tokens():
    return [Token('R'), Token('Y')]

#~~~~~~~~~~~~~~~~~~~~~
def initialize_board():
    board_coordinates = {}
    columns = [1, 2, 3, 4, 5, 6, 7]
    rows = [1, 2, 3, 4, 5, 6]
    for column in columns:
        for row in rows:
            board_coordinates[str(column) + str(row)] = ' '
    board = Board(board_coordinates)
    return board

#~~~~~~~~~~~~~~~~~~~~~
def call_moves(move_list, token_objects, board):
    move_index = 0
    while move_index < len(move_list):
        for token in token_objects:
            move = move_list[move_index]
            board.check_if_filled(move, token.color)
            move_index += 1
            print(board)
            input('')

#~~~~~~~~~~~~~~~~~~~~~
def main():
    board = initialize_board()
    token_objects = initialize_tokens()

    move_list = read_game_moves_file()

    call_moves(move_list, token_objects, board)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
columns = [1, 2, 3, 4, 5, 6, 7]
rows = [1, 2, 3, 4, 5, 6]


main()





#

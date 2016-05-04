

class ListListTTTBoard:
    """
    X| |
     |X|O
     | |

    [
        ['X', ' ', ' '],
        [' ', 'X', 'O'],
        [' ', ' ', ' '],
    ]
    """

    def __init__(self):
        self.rows = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def place(self, x, y, player):
        if self.rows[y][x] == ' ':
            self.rows[y][x] = player

    def won(self):
        l = self.rows
        possibilities = []
        for y in range(0, 3):
            possibilities.append(''.join(l[y][0:3]))
            possibilities.append(''.join([l[0][y], l[1][y], l[2][y]]))
        possibilities.append(''.join([l[0][0], l[1][1], l[2][2]]))
        possibilities.append(''.join([l[2][0], l[1][1], l[0][2]]))
        print(possibilities)
        if 'XXX' in possibilities: return 'X'
        if 'OOO' in possibilities: return 'O'

    def __str__(self):
        row1 = ' | '.join(row for row in self.rows[0])
        row2 = ' | '.join(row for row in self.rows[1])
        row3 = ' | '.join(row for row in self.rows[2])
        return "\n{}\n---------\n{}\n---------\n{}\n".format(row1, row2, row3)


class DictTTTBoard:
    """
    {
        'a1': 'X', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': 'X', 'c2': 'O',
        'a3': ' ', 'b3': ' ', 'c3': ' ',
    }
    """

    def __init__(self):
        self.pos_to_token = {
            'a1': ' ', 'b1': ' ', 'c1': ' ',
            'a2': ' ', 'b2': ' ', 'c2': ' ',
            'a3': ' ', 'b3': ' ', 'c3': ' ',
        }

    def place(self, x, y, token):
        if x == 0: x = 'a'
        if x == 1: x = 'b'
        if x == 2: x = 'c'
        if y == 0: y = '1'
        if y == 1: y = '2'
        if y == 2: y = '3'
        coordinate = str(x + y)
        if self.pos_to_token[coordinate] == ' ':
            self.pos_to_token[coordinate] = token

    def won(self):
        d = self.pos_to_token
        possibilities = [
            (d['a1'] + d['b1'] + d['c1']),
            (d['a2'] + d['b2'] + d['c2']),
            (d['a3'] + d['b3'] + d['c3']),
            (d['a1'] + d['a2'] + d['a3']),
            (d['b1'] + d['b2'] + d['b3']),
            (d['c1'] + d['c2'] + d['c3']),
            (d['a1'] + d['b2'] + d['c3']),
            (d['c3'] + d['b2'] + d['a3'])
            ]
        if 'XXX' in possibilities: return 'X'
        if 'OOO' in possibilities: return 'O'

    def __str__(self):
        d = self.pos_to_token
        row1 = ' | '.join([d['a1'], d['b1'], d['c1']])
        row2 = ' | '.join([d['a2'], d['b2'], d['c2']])
        row3 = ' | '.join([d['a3'], d['b3'], d['c3']])
        return "\n{}\n---------\n{}\n---------\n{}\n".format(row1, row2, row3)

class CoordsTTTBoard:
    """[(0, 0, 'X'), (1, 1, 'X'), (2, 1, 'O')]"""

    def __init__(self):
        self.x_y_token_triplets = []

    def place(self, x, y, player):
        coordinate = (x, y, player)
        if coordinate not in self.x_y_token_triplets:
            self.x_y_token_triplets.append(coordinate)

    def won(self):
        l = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        for x, y, token in self.x_y_token_triplets:
            l[y][x] = token
        possibilities = [
            (l[0][0] + l[0][1] + l[0][2]),
            (l[1][0] + l[1][1] + l[1][2]),
            (l[2][0] + l[2][1] + l[2][2]),
            (l[0][0] + l[1][0] + l[2][0]),
            (l[0][1] + l[1][1] + l[2][1]),
            (l[0][2] + l[1][2] + l[2][2]),
            (l[0][0] + l[1][1] + l[2][2]),
            (l[2][0] + l[1][1] + l[0][2]),
            ]
        if 'XXX' in possibilities: return 'X'
        if 'OOO' in possibilities: return 'O'

    def __str__(self):
        l = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        for x, y, token in self.x_y_token_triplets:
            l[y][x] = token
        row1 = ' | '.join(row for row in l[0])
        row2 = ' | '.join(row for row in l[1])
        row3 = ' | '.join(row for row in l[2])
        return "\n{}\n---------\n{}\n---------\n{}\n".format(row1, row2, row3)


def play(board):
    board.place(1, 1, 'X')
    print(board)
    board.place(0, 0, 'O')
    print(board)
    board.place(1, 0, 'X')
    assert str(board) == "\nO | X |  \n---------\n  | X |  \n---------\n  |   |  \n"
    print(board)
    board.place(0, 2, 'O')
    print(board)
    # assert board.won() is None
    board.place(1, 2, 'X')
    print(board)
    # assert board.won() == 'X'
    winner = board.won()
    print("Winner is: ", winner)


def main():
    board1 = ListListTTTBoard()
    play(board1)
    board2 = DictTTTBoard()
    play(board2)
    board3 = CoordsTTTBoard()
    play(board3)

if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"[{self.y}, {self.x}]"


@dataclass
class Piece:
    color: str
    position: Position
    g: 'Game' = None

    def __init__(self, color):
        self.color = color

    color: str

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def possible_moves(self, cur_pos: Position) -> List[Position]:
        pass


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self) -> str:
        return '♙' if self.color == 'white' else '♟'

    def possible_moves(self, cur_pos: Position) -> List[Position]:
        moves = []
        x, y = cur_pos.x, cur_pos.y

        if self.color == 'white':
            if y + 1 < 8 and g.board[y + 1][x] is None:
                moves.append(Position(x, y + 1))
                if (y == 1) and g.board[y + 2][x] is None:
                    moves.append(Position(x, y + 2))
            for ix in [-1, 1]:
                if 0 <= x + ix < 8 and 0 <= y + 1 < 8 and g.board[y + 1][x + ix] is not None and \
                        g.board[y + 1][x + ix].color != self.color:
                    moves.append(Position(x + ix, y + 1))
        else:
            if y - 1 <= 0 and g.board[y - 1][x] is None:
                moves.append(Position(x, y - 1))
                if (y == 6) and g.board[y - 2][x] is None:
                    moves.append(Position(x, y - 2))
            for ix in [-1, 1]:
                if 0 <= x + ix < 8 and 0 <= y - 1 < 8 and g.board[y - 1][x + ix] is not None and \
                        g.board[y - 1][x + ix].color != self.color:
                    moves.append(Position(x + ix, y - 1))
        return moves


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self) -> str:
        return '♖' if self.color == 'white' else '♜'

    def possible_moves(self, cur_pos: Position) -> List[Position]:
        moves = []
        for ix in [-1, 1]:
            x, y = cur_pos.x + ix, cur_pos.y
            while 0 <= x < 8:
                if g.board[y][x] is None:
                    moves.append(Position(x, y))
                elif g.board[y][x].color != self.color:
                    moves.append(Position(x, y))
                    break
                else:
                    break
                x += ix
        for iy in [-1, 1]:
            x, y = cur_pos.x, cur_pos.y + iy
            while 0 <= y < 8:
                if g.board[y][x] is None:
                    moves.append(Position(x, y))
                elif g.board[y][x].color != self.color:
                    moves.append(Position(x, y))
                    break
                else:
                    break
                y += iy
        return moves


class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self) -> str:
        return '♔' if self.color == 'white' else '♚'

    def possible_moves(self, cur_pos: Position) -> List[Position]:
        moves = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x, new_y = cur_pos.x + dx, cur_pos.y + dy
                if 0 <= new_x < 8 and 0 <= new_y < 8 and (
                        g.board[new_y][new_x] is None or g.board[new_y][new_x].color != self.color):
                    moves.append(Position(new_x, new_y))
        return moves


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self) -> str:
        return '♕' if self.color == 'white' else '♛'

    def possible_moves(self, cur_pos: Position) -> List[Position]:
        moves = []
        x, y = cur_pos.x, cur_pos.y
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    new_x, new_y = x + dx, y + dy
                    while 0 <= new_x < 8 and 0 <= new_y < 8:
                        if g.board[new_y][new_x] is None:
                            moves.append(Position(new_x, new_y))
                        elif g.board[new_y][new_x].color != self.color:
                            moves.append(Position(new_x, new_y))
                            break
                        else:
                            break
                        new_x += dx
                        new_y += dy
        return moves


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self) -> str:
        return '♗' if self.color == 'white' else '♝'

    def possible_moves(self, cur_pos: Position) -> List[Position]:
        moves = []
        x, y = cur_pos.x, cur_pos.y
        for dx in [-1, 1]:
            for dy in [-1, 1]:
                new_x, new_y = x + dx, y + dy
                while 0 <= new_x < 8 and 0 <= new_y < 8:
                    if g.board[new_y][new_x] is None:
                        moves.append(Position(new_x, new_y))
                    elif g.board[new_y][new_x].color != self.color:
                        moves.append(Position(new_x, new_y))
                        break
                    else:
                        break
                    new_x += dx
                    new_y += dy
        return moves


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self) -> str:
        return '♘' if self.color == 'white' else '♞'

    def possible_moves(self, cur_pos: Position) -> List[Position]:
        moves = []
        x, y = cur_pos.x, cur_pos.y
        for dx in [-2, 2]:
            for dy in [-1, 1]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if g.board[new_y][new_x] is None or g.board[new_y][new_x].color != self.color:
                        moves.append(Position(new_x, new_y))
        for dx in [-1, 1]:
            for dy in [-2, 2]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if g.board[new_y][new_x] is None or g.board[new_y][new_x].color != self.color:
                        moves.append(Position(new_x, new_y))
        return moves


class Game:
    board: List[List[Piece]]

    def __init__(self):
        Q = Queen
        K = King
        N = Knight
        P = Pawn
        B = Bishop
        R = Rook
        w = "white"
        b = "black"

        self.board = [
            [R(w), N(w), B(w), Q(w), K(w), B(w), N(w), R(w)],
            [P(w), P(w), P(w), P(w), P(w), P(w), P(w), P(w)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [P(b), P(b), P(b), P(b), P(b), P(b), P(b), P(b)],
            [R(b), N(b), B(b), Q(b), K(b), B(b), N(b), R(b)]
        ]

        for y in range(8):
            for x in range(8):
                piece = self.board[y][x]
                if piece is not None:
                    piece.p = Position(x, y)
                    piece.g = self

    def print(self):
        output = ""
        for line in self.board:
            for piece in line:
                if piece is not None:
                    output += str(piece) + " "
                else:
                    output += "    "
            output += '\n'
        print(output)


g = Game()
possible_nums = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7}
possible_letters = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "h": 6, "g": 7}
g.print()

while True:
    try:
        # input module
        start = input("Choose a figure: ")
        end = input("Chose where to place it: ")
        if len(start) > 2 or not start[0] in possible_letters or not start[1] in possible_nums \
                or len(end) > 2 or not end[0] in possible_letters or not end[1] in possible_nums:
            raise Exception('Input Error')

        # output module
        print(possible_letters[start[0]], possible_nums[start[1]])
        print(possible_letters[end[0]], possible_nums[end[1]])
        g.print()
    except Exception as inst:
        print(inst)
        s = input()

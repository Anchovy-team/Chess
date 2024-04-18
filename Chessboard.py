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
            if y + 1 < 8 and self.g.board[y + 1][x] is None:
                moves.append(Position(x, y + 1))
                if (y == 1) and self.g.board[y + 2][x] is None:
                    moves.append(Position(x, y + 2))
            for ix in [-1, 1]:
                if 0 <= x + ix < 8 and 0 <= y + 1 < 8 and self.g.board[y + 1][x + ix] is not None and \
                        self.g.board[y + 1][x + ix].color != self.color:
                    moves.append(Position(x + ix, y + 1))
        else:
            if y - 1 <= 0 and self.g.board[y - 1][x] is None:
                moves.append(Position(x, y - 1))
                if (y == 6) and self.g.board[y - 2][x] is None:
                    moves.append(Position(x, y - 2))
            for ix in [-1, 1]:
                if 0 <= x + ix < 8 and 0 <= y - 1 < 8 and self.g.board[y - 1][x + ix] is not None and \
                        self.g.board[y - 1][x + ix].color != self.color:
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
                if self.g.board[y][x] is None:
                    moves.append(Position(x, y))
                elif self.g.board[y][x].color != self.color:
                    moves.append(Position(x, y))
                    break
                else:
                    break
                x += ix
        for iy in [-1, 1]:
            x, y = cur_pos.x, cur_pos.y + iy
            while 0 <= y < 8:
                if self.g.board[y][x] is None:
                    moves.append(Position(x, y))
                elif self.g.board[y][x].color != self.color:
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
                        self.g.board[new_y][new_x] is None or self.g.board[new_y][new_x].color != self.color):
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
                        if self.g.board[new_y][new_x] is None:
                            moves.append(Position(new_x, new_y))
                        elif self.g.board[new_y][new_x].color != self.color:
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
                    if self.g.board[new_y][new_x] is None:
                        moves.append(Position(new_x, new_y))
                    elif self.g.board[new_y][new_x].color != self.color:
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
                    if self.g.board[new_y][new_x] is None or self.g.board[new_y][new_x].color != self.color:
                        moves.append(Position(new_x, new_y))
        for dx in [-1, 1]:
            for dy in [-2, 2]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if self.g.board[new_y][new_x] is None or self.g.board[new_y][new_x].color != self.color:
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
            [None, None, None, K(w), None, None, None, None],
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
                    
    def clean_board(self):
        self.board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]
    @staticmethod
    def is_check_mate() -> bool:
        # FIXME
        return False

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

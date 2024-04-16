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
    def __init__(self, color, position):
        self.color = color
        self.position = position
    color: str

    @abstractmethod
    def __str__(self) -> str:
        pass


    def possible_moves(self, current_position: Position, board: List[List]) -> List[Position]:
        pass


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self) -> str:
        return '♙' if self.color == 'white' else '♟'


    def possible_moves(self, current_position: Position, board: List[List[Piece]]) -> List[Position]:
        moves = []
        x, y = current_position.x, current_position.y

        if self.color == 'white':

            if y + 1 < 8 and board[y + 1][x] is None:
                moves.append(Position(x, y + 1))
                if (y == 1) and  board[y + 2][x] is None:
                    moves.append(Position(x, y + 2))
            for ix in [-1, 1]:
                if 0 <= x + ix < 8 and 0 <= y + 1 < 8 and board[y+1][x+ix] is not None and\
                        board[y+1][x+ix].color != self.color:
                    moves.append(Position(x+ix, y+1))
        else:
            if y -1 <= 0 and board[y - 1][x] is None:
                moves.append(Position(x, y - 1))
                if (y == 6) and  board[y -2][x] is None:
                    moves.append(Position(x, y - 2))
            for ix in [-1, 1]:
                if 0 <= x + ix < 8 and 0 <= y -1 < 8 and board[y-1][x+ix] is not None and \
                        board[y-1][x+ix].color != self.color:
                    moves.append(Position(x+ix, y-1))
        return moves


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self) -> str:
        return '♖' if self.color == 'white' else '♜'


    def possible_moves(self, current_position: Position, board: List[List[Piece]]) -> List[Position]:
        moves = []
        for ix in [-1, 1]:
            x, y = current_position.x + ix, current_position.y
            while 0 <= x < 8:
                if board[y][x] is None:
                    moves.append(Position(x, y))
                elif board[y][x].color != self.color:
                    moves.append(Position(x, y))
                    break
                else:
                    break
                x += ix
        for iy in [-1, 1]:
            x, y = current_position.x, current_position.y + iy
            while 0 <= y < 8:
                if board[y][x] is None:
                    moves.append(Position(x, y))
                elif board[y][x].color != self.color:
                    moves.append(Position(x, y))
                    break
                else:
                    break
                y += iy

        return moves


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self) -> str:
        return '♔' if self.color == 'white' else '♚'


    def possible_moves(self, current_position: Position, board: List[List[Piece]]) -> List[Position]:
        moves = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x, new_y = current_position.x + dx, current_position.y + dy
                if 0 <= new_x < 8 and 0 <= new_y < 8 and (board[new_y][new_x] is None or board[new_y][new_x].color != self.color):
                    moves.append(Position(new_x, new_y))
        return moves


class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self) -> str:
        return '♕' if self.color == 'white' else '♛'

    def possible_moves(self, current_position: Position, board: List[List[Piece]]) -> List[Position]:
        moves = []
        x, y = current_position.x, current_position.y
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    new_x, new_y = x + dx, y + dy
                    while 0 <= new_x < 8 and 0 <= new_y < 8:
                        if board[new_y][new_x] is None:
                            moves.append(Position(new_x, new_y))
                        elif board[new_y][new_x].color != self.color:
                            moves.append(Position(new_x, new_y))
                            break
                        else:
                            break
                        new_x += dx
                        new_y += dy
        return moves


class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self) -> str:
        return '♗' if self.color == 'white' else '♝'

    def possible_moves(self, current_position: Position, board: List[List[Piece]]) -> List[Position]:
        moves = []
        x, y = current_position.x, current_position.y
        for dx in [-1, 1]:
            for dy in [-1, 1]:
                new_x, new_y = x + dx, y + dy
                while 0 <= new_x < 8 and 0 <= new_y < 8:
                    if board[new_y][new_x] is None:
                        moves.append(Position(new_x, new_y))
                    elif board[new_y][new_x].color != self.color:
                        moves.append(Position(new_x, new_y))
                        break
                    else:
                        break
                    new_x += dx
                    new_y += dy
        return moves


class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self) -> str:
        return '♘' if self.color == 'white' else '♞'


    def possible_moves(self, current_position: Position, board: List[List[Piece]]) -> List[Position]:
        moves = []
        x, y = current_position.x, current_position.y
        for dx in [-2, 2]:
            for dy in [-1, 1]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if board[new_y][new_x] is None or board[new_y][new_x].color != self.color:
                        moves.append(Position(new_x, new_y))
        for dx in [-1, 1]:
            for dy in [-2, 2]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if board[new_y][new_x] is None or board[new_y][new_x].color != self.color:
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
            [R(w, (0, 0)), N(w, (0, 1)), B(w, (0, 2)), Q(w, (0, 3)), K(w, (0, 4)), B(w, (0, 5)), N(w, (0, 6)), R(w, (0, 7))],
            [P(w, (1, 0)), P(w, (1, 1)), P(w, (1, 2)), P(w, (1, 3)), P(w, (1, 4)), P(w, (1, 5)), P(w, (1, 6)), P(w, (1, 7))],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [P(b, (6, 0)), P(b, (6, 1)), P(b, (6, 2)), P(b, (6, 3)), P(b, (6, 4)), P(b, (6, 5)), P(b, (6, 6)), P(b, (6, 7))],
            [R(b, (7, 0)), N(b, (7, 1)), B(b, (7, 2)), Q(b, (7, 3)), K(b, (7, 4)), B(b, (7, 5)), N(b, (7, 6)), R(b, (7, 7))]
        ]

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



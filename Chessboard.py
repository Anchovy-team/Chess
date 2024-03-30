from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class Position:
    x: int
    y: int


@dataclass
class Piece(ABC):
    color: str

    @abstractmethod
    def __str__(self) -> str:
        pass


class Pawn(Piece):
    def __str__(self) -> str:
        return '♙' if self.color == 'white' else '♟'


class Rook(Piece):
    def __str__(self) -> str:
        return '♖' if self.color == 'white' else '♜'


class King(Piece):
    def __str__(self) -> str:
        return '♔' if self.color == 'white' else '♚'


class Queen(Piece):
    def __str__(self) -> str:
        return '♕' if self.color == 'white' else '♛'


class Bishop(Piece):
    def __str__(self) -> str:
        return '♗' if self.color == 'white' else '♝'


class Knight(Piece):
    def __str__(self) -> str:
        return '♘' if self.color == 'white' else '♞'


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
g.print()

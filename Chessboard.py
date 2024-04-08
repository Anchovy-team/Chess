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
posssible_nums = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7}
posssible_letters = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "h": 6, "g":7}
g.print()

while True:
    try:
        # input module
        start = input("Choose a figure: ")
        end = input("Chose where to place it: ")
        if len(start) > 2 or not start[0] in posssible_letters or not start[1] in posssible_nums\
                or len(end) > 2 or not end[0] in posssible_letters or not end[1] in posssible_nums:
            raise Exception('Input Error')

        # output module
        print(posssible_letters[start[0]], posssible_nums[start[1]])
        print(posssible_letters[end[0]], posssible_nums[end[1]])
        g.print()
    except Exception as inst:
        print(inst)
        s = input()

from abc import abstractmethod
from dataclasses import dataclass
from typing import List
import chevron


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"[{self.y}, {self.x}]"

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False


@dataclass
class Piece:
    color: str
    position: Position
    g: 'Game' = None

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def possible_moves(self) -> List[Position]:
        pass


class Pawn(Piece):
    moved2cells: bool = False

    def __init__(self, color):
        super().__init__(color)

    def __str__(self) -> str:
        return '♙' if self.color == 'white' else '♟'

    def possible_moves(self) -> List[Position]:
        moves = []
        x, y = self.position.x, self.position.y

        if self.color == 'white':
            if (x > 0 and not (self.g.board[y][x - 1] is None) and self.g.board[y][x - 1].__class__.__name__ == 'Pawn'
                    and self.g.board[y][x - 1].color != 'white' and self.g.board[y][x - 1].moved2cells):
                moves.append(Position(x - 1, y + 1))
            if (x < 7 and not (self.g.board[y][x + 1] is None) and self.g.board[y][x + 1].__class__.__name__ == 'Pawn'
                    and self.g.board[y][x + 1].color != 'white' and self.g.board[y][x + 1].moved2cells):
                moves.append(Position(x + 1, y + 1))
            if y + 1 < 8 and self.g.board[y + 1][x] is None:
                moves.append(Position(x, y + 1))
                if (y == 1) and self.g.board[y + 2][x] is None:
                    moves.append(Position(x, y + 2))
            for ix in [-1, 1]:
                if 0 <= x + ix < 8 and 0 <= y + 1 < 8 and self.g.board[y + 1][x + ix] is not None and \
                        self.g.board[y + 1][x + ix].color != self.color:
                    moves.append(Position(x + ix, y + 1))
        else:
            if (x > 0 and not (self.g.board[y][x - 1] is None) and self.g.board[y][x - 1].__class__.__name__ == 'Pawn'
                    and self.g.board[y][x - 1].color != 'black' and self.g.board[y][x - 1].moved2cells):
                moves.append(Position(x - 1, y - 1))
            if (x < 7 and not (self.g.board[y][x + 1] is None) and self.g.board[y][x + 1].__class__.__name__ == 'Pawn'
                    and self.g.board[y][x + 1].color != 'black' and self.g.board[y][x + 1].moved2cells):
                moves.append(Position(x + 1, y - 1))
            if y - 1 >= 0 and self.g.board[y - 1][x] is None:
                moves.append(Position(x, y - 1))
                if (y == 6) and self.g.board[y - 2][x] is None:
                    moves.append(Position(x, y - 2))
            for ix in [-1, 1]:
                if 0 <= x + ix < 8 and 0 <= y - 1 < 8 and self.g.board[y - 1][x + ix] is not None and \
                        self.g.board[y - 1][x + ix].color != self.color:
                    moves.append(Position(x + ix, y - 1))
        return moves


class Rook(Piece):
    Rook_move:bool = False

    def __init__(self, color):
        super().__init__(color)

    def __str__(self) -> str:
        return '♖' if self.color == 'white' else '♜'

    def possible_moves(self) -> List[Position]:
        moves = []
        for ix in [-1, 1]:
            x, y = self.position.x + ix, self.position.y
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
            x, y = self.position.x, self.position.y + iy
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
    first_check: bool = False
    king_moved: bool = False

    def __init__(self, color):
        super().__init__(color)

    def __str__(self) -> str:
        return '♔' if self.color == 'white' else '♚'

    def possible_moves(self) -> List[Position]:
        moves = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                else:
                    new_x, new_y = self.position.x + dx, self.position.y + dy
                    if 0 <= new_x < 8 and 0 <= new_y < 8 and (
                            self.g.board[new_y][new_x] is None or self.g.board[new_y][new_x].color != self.color):
                        moves.append(Position(new_x, new_y))

        # CASTLING
        if not self.first_check and not self.king_moved:
            if self.color == 'white':
                if self.g[5][0] is None and self.g[6][0] is None\
                        and self.g[7][0].__class__.__name__ == 'Rook' and self.g[7][0].color == 'white' and not self.g[7][0].rook_moved:
                    moves.append(Position(6, 0))
                if self.g[3][0] is None and self.g[2][0] is None and self.g[1][0] is None \
                        and self.g[0][0].__class__.__name__ == 'Rook' and self.g[7][0].color == 'white' and not self.g[0][0].rook_moved:
                    moves.append(Position(1, 0))
            else:
                if self.g[5][7] is None and self.g[6][7] is None\
                        and self.g[7][7].__class__.__name__ == 'Rook' and self.g[7][7].color == 'black' and not self.g[0][7].rook_moved:
                    moves.append(Position(6, 7))
                if self.g[3][7] is None and self.g[2][7] is None and self.g[1][7] is None \
                        and self.g[0][7].__class__.__name__ == 'Rook' and self.g[7][7].color == 'black' and not self.g[0][7].rook_moved:
                    moves.append(Position(1, 7))

        return moves


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self) -> str:
        return '♕' if self.color == 'white' else '♛'

    def possible_moves(self) -> List[Position]:
        moves = []
        x, y = self.position.x, self.position.y
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

    def possible_moves(self) -> List[Position]:
        moves = []
        x, y = self.position.x, self.position.y
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


@dataclass
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self) -> str:
        return '♘' if self.color == 'white' else '♞'

    def possible_moves(self) -> List[Position]:
        moves = []
        x, y = self.position.x, self.position.y
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
    board: List[List[Piece or None]]

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
                if not (piece is None):
                    piece.position = Position(x, y)
                    piece.g = self

    def move(self, start: Position, end: Position):
        dx, dy = start.x, start.y
        edx, edy = end.x, end.y
        if self.board[dy][dx] is None:
            raise Exception('No piece here')
        elif end not in self.board[dy][dx].possible_moves():
            raise Exception('You can not go there')
        else:
            piece = self.board[dy][dx]
            piece.position = Position(edx, edy)
            if piece.__class__.__name__ == 'Rook':
                self.board[dy][dx].rook_moved = True
            if piece.__class__.__name__ == 'King':
                self.board[dy][dx].king_moved = True
            if piece.__class__.__name__ == 'Pawn':
                if abs(edx - dx) == 1 and abs(edy - dy) == 1 and self.board[edy][edx] is None:
                    self.board[dy][edx] = None
                piece.moved2cells = abs(dy - edy) == 2

            self.board[edy][edx] = self.board[dy][dx]
            self.board[dy][dx] = None

    def master_move(self, start: Position, end: Position):
        dx, dy = start.x, start.y
        edx, edy = end.x, end.y
        piece = self.board[dy][dx]
        piece.position = Position(edx, edy)
        self.board[edy][edx] = self.board[dy][dx]
        self.board[dy][dx] = None

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

    def is_check(self, color: str) -> bool:
        all_possible_moves = []
        for line in self.board:
            for piece in line:
                if not (piece is None) and piece.color != color:
                    all_possible_moves += piece.possible_moves()

        king_position = Position(0, 0)
        for line in self.board:
            for piece in line:
                if not (piece is None) and piece.__class__.__name__ == "King" and piece.color == color:
                    king_position = piece.position
        if king_position in all_possible_moves:
            self[king_position.x][king_position.y].first_check = True
        return king_position in all_possible_moves

    def is_check_mate(self) -> str:
        end_game = True
        if self.is_check('black'):
            for line in self.board:
                for piece in line:
                    if not (piece is None) and piece.color == 'black':
                        cur_pos = piece.position
                        for move in piece.possible_moves():
                            replaced_piece = self.board[move.y][move.x]
                            self.master_move(cur_pos, move)
                            if not self.is_check('black'):
                                end_game = False
                            self.master_move(move, cur_pos)
                            self.board[move.y][move.x] = replaced_piece
                            if not end_game:
                                return 'continue'
            return 'black'

        elif self.is_check('white'):
            for line in self.board:
                for piece in line:
                    if not (piece is None) and piece.color == 'white':
                        cur_pos = piece.position
                        for move in piece.possible_moves():
                            replaced_piece = self.board[move.y][move.x]
                            self.master_move(cur_pos, move)
                            if not self.is_check('white'):
                                end_game = False
                            self.master_move(move, cur_pos)
                            self.board[move.y][move.x] = replaced_piece
                            if not end_game:
                                return 'continue'
            return 'white'

        return 'continue'

    def is_draw(self) -> bool:
        cnt_pieces = 0
        for line in self.board:
            for piece in line:
                if not (piece is None):
                    cnt_pieces += 1
        if cnt_pieces == 2:
            return True

        no_moves_black = True
        no_moves_white = True
        for line in self.board:
            for piece in line:
                if not (piece is None) and piece.color == 'black':
                    cur_pos = piece.position
                    for move in piece.possible_moves():
                        replaced_piece = self.board[move.y][move.x]
                        self.master_move(cur_pos, move)
                        if not self.is_check('black'):
                            self.master_move(move, cur_pos)
                            self.board[move.y][move.x] = replaced_piece
                            no_moves_black = False
                            break
                        self.master_move(move, cur_pos)
                        self.board[move.y][move.x] = replaced_piece

        for line in self.board:
            for piece in line:
                if not (piece is None) and piece.color == 'white':
                    cur_pos = piece.position
                    for move in piece.possible_moves():
                        replaced_piece = self.board[move.y][move.x]
                        self.master_move(cur_pos, move)
                        if not self.is_check('white'):
                            self.master_move(move, cur_pos)
                            self.board[move.y][move.x] = replaced_piece
                            no_moves_white = False
                            break
                        self.master_move(move, cur_pos)
                        self.board[move.y][move.x] = replaced_piece

        if no_moves_black or no_moves_white:
            return True
        else:
            return False

    def print(self):
        output = "\n"
        i = 1
        for line in self.board[::-1]:
            output += str(9 - i) + "  "
            for piece in line:
                if piece is not None:
                    output += str(piece) + "  "
                else:
                    output += " " + "  "
            output += "\n"
            i += 1
        output += ("   A  " + "B  " + "C  " "D  " + "E  " + "F  " +
                   "G  " + "H\n")
        print(output)

    def print_svg(self):
        render_list = []
        for rows in self.board:
            for piece in rows:
                if piece:
                    svg_piece = ""
                    match piece.__class__.__name__:
                        case "Queen":
                            if piece.color == "black":
                                svg_piece = open("Pieces/Chess_qdt45.svg", "r")

                            else:
                                svg_piece = open("Pieces/Chess_qlt45.svg", "r")
                        case "Knight":
                            if piece.color == "black":
                                svg_piece = open("Pieces/Chess_ndt45.svg", "r")

                            else:
                                svg_piece = open("Pieces/Chess_nlt45.svg", "r")
                        case "Bishop":
                            if piece.color == "black":
                                svg_piece = open("Pieces/Chess_bdt45.svg", "r")

                            else:
                                svg_piece = open("Pieces/Chess_blt45.svg", "r")
                        case "Pawn":
                            if piece.color == "black":
                                svg_piece = open("Pieces/Chess_pdt45.svg", "r")

                            else:
                                svg_piece = open("Pieces/Chess_plt45.svg", "r")
                        case "Rook":
                            if piece.color == "black":
                                svg_piece = open("Pieces/Chess_rdt45.svg", "r")

                            else:
                                svg_piece = open("Pieces/Chess_rlt45.svg", "r")
                        case "King":
                            if piece.color == "black":
                                svg_piece = open("Pieces/Chess_kdt45.svg", "r")

                            else:
                                svg_piece = open("Pieces/Chess_klt45.svg", "r")
                    render_list.append([piece.position.x * 45, (7 - piece.position.y) * 45, str(svg_piece.read())])
                    svg_piece.close()

        data = {"items": render_list}
        svg_board = open("new_board.svg", "w")
        temp = open("clean_board.svg", 'r')
        svg_board.write(chevron.render(temp, data))
        temp.close()
        svg_board.close()

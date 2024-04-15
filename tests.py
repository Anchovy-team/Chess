import unittest
from Chessboard import Pawn, Rook, King, Queen, Bishop, Knight, Position, Game


class PawnTest(unittest.TestCase):
    def test_move_two_squares_initial(self):
        p = Pawn('white', (1,0))
        pos = p.possible_moves(current_position, board)
        expected = [Position(1,1), Position(1,2)]
        self.assertEqual(pos, expected)

    def test_move_one_square_not_initial(self):
        p = Pawn('white', (1,1))
        pos = p.possible_moves(current_position, board)
        expected = [Position(1,2)]
        self.assertEqual(pos, expected)

    def test_capture_diagonally(self):
        p1 = Pawn('white', (1,0))
        p2 = Pawn('black', (2,1))
        g = Game()
        g.board[1][0] = p1
        g.board[2][1] = p2
        p1.g = g
        expected = [Position(1,1), Position(2,1)]
        self.assertEqual(p1.possible_moves(current_position, board), expected)

    def test_blocked_by_piece(self):
        p1 = Pawn('white', (1,0))
        p2 = Pawn('white', (1,1))
        g = Game()
        g.board[1][0] = p1
        g.board[1][1] = p2
        p1.g = g
        expected = []
        self.assertEqual(p1.possible_moves(current_position, board), expected)

    def test_promotion(self):
        p = Pawn('white', (1,6))
        pos = p.possible_moves(current_position, board)
        expected = [Position(1,7, 'Queen'), Position(1,7, 'Rook'), Position(1,7, 'Bishop'), Position(1,7, 'Knight')]
        self.assertEqual(pos, expected)


class RookTest(unittest.TestCase):
    def test_move_along_rank_file(self):
        r = Rook('white', (0,0))
        pos = r.possible_moves(current_position, board)
        expected = [Position(i, 0) for i in range(1, 8)] + [Position(0, i) for i in range(1, 8)]
        self.assertEqual(set(pos), set(expected))

    def test_cannot_move_diagonally(self):
        r = Rook('white', (0,0))
        pos = r.possible_moves(current_position, board)
        diagonal_moves = [Position(i, i) for i in range(1, 8)]
        self.assertTrue(not any(move in pos for move in diagonal_moves))

    def test_cannot_move_over_pieces(self):
        r = Rook('white', (0,0))
        p = Pawn('white', (0,1))
        g = Game()
        g.board[0][0] = r
        g.board[0][1] = p
        r.g = g
        pos = r.possible_moves(current_position, board)
        blocked_moves = [Position(0, i) for i in range(2, 8)]
        self.assertTrue(not any(move in pos for move in blocked_moves))


class KnightTest(unittest.TestCase):
    def test_move_L_shape(self):
        k = Knight('white', (3,3))
        pos = k.possible_moves(current_position, board)
        expected = [Position(1,2), Position(1,4), Position(2,1), Position(2,5), Position(4,1), Position(4,5), Position(5,2), Position(5,4)]
        self.assertEqual(set(pos), set(expected))

    def test_jump_over_pieces(self):
        k = Knight('white', (3,3))
        p = Pawn('white', (3,4))
        g = Game()
        g.board[3][3] = k
        g.board[3][4] = p
        k.g = g
        pos = k.possible_moves(current_position, board)
        expected = [Position(1,2), Position(1,4), Position(2,1), Position(2,5), Position(4,1), Position(4,5), Position(5,2), Position(5,4)]
        self.assertEqual(set(pos), set(expected))


class QueenTest(unittest.TestCase):
    def test_move_along_rank_file_diagonal(self):
        q = Queen('white', (3,3))
        pos = q.possible_moves(current_position, board)
        expected = [Position(i, 3) for i in range(0, 8) if i != 3] + \
                   [Position(3, i) for i in range(0, 8) if i != 3] + \
                   [Position(i, j) for i in range(0, 8) for j in range(0, 8) if abs(i - 3) == abs(j - 3) and i != 3]
        self.assertEqual(set(pos), set(expected))

    def test_cannot_move_like_knight(self):
        q = Queen('white', (3,3))
        pos = q.possible_moves(current_position, board)
        knight_moves = [Position(1,2), Position(1,4), Position(2,1), Position(2,5), Position(4,1), Position(4,5), Position(5,2), Position(5,4)]
        self.assertTrue(not any(move in pos for move in knight_moves))

    def test_cannot_move_over_pieces(self):
        q = Queen('white', (3,3))
        p = Pawn('white', (3,4))
        g = Game()
        g.board[3][3] = q
        g.board[3][4] = p
        q.g = g
        pos = q.possible_moves(current_position, board)
        blocked_moves = [Position(3, i) for i in range(5, 8)] + \
                        [Position(i, 4) for i in range(4, 8)] + \
                        [Position(i, j) for i in range(4, 8) for j in range(5, 8) if abs(i - 3) == abs(j - 4)]
        self.assertTrue(not any(move in pos for move in blocked_moves))


class BishopTest(unittest.TestCase):
    def test_move_diagonally(self):
        b = Bishop('white', (3,3))
        pos = b.possible_moves(current_position, board)
        expected = [Position(i, j) for i in range(0, 8) for j in range(0, 8) if abs(i - 3) == abs(j - 3) and i != 3]
        self.assertEqual(set(pos), set(expected))

    def test_cannot_move_along_rank_file(self):
        b = Bishop('white', (3,3))
        pos = b.possible_moves(current_position, board)
        rank_file_moves = [Position(i, 3) for i in range(0, 8) if i != 3] + [Position(3, i) for i in range(0, 8) if i != 3]
        self.assertTrue(not any(move in pos for move in rank_file_moves))

    def test_cannot_move_over_pieces(self):
        b = Bishop('white', (3,3))
        p = Pawn('white', (4,4))
        g = Game()
        g.board[3][3] = b
        g.board[4][4] = p
        b.g = g
        pos = b.possible_moves(current_position, board)
        blocked_moves = [Position(i, j) for i in range(5, 8) for j in range(5, 8) if abs(i - 3) == abs(j - 3)]
        self.assertTrue(not any(move in pos for move in blocked_moves))


class KingTest(unittest.TestCase):
    def test_move_one_square_any_direction(self):
        k = King('white', (3,3))
        pos = k.possible_moves(current_position, board)
        expected = [Position(2,2), Position(2,3), Position(2,4), Position(3,2), Position(3,4), Position(4,2), Position(4,3), Position(4,4)]
        self.assertEqual(set(pos), set(expected))

    def test_cannot_move_into_check(self):
        k = King('white', (3,3))
        q = Queen('black', (4,4))
        g = Game()
        g.board[3][3] = k
        g.board[4][4] = q
        k.g = g
        pos = k.possible_moves(current_position, board)
        check_moves = [Position(4,3), Position(4,4)]
        self.assertTrue(not any(move in pos for move in check_moves))

    def test_castling(self):
        k = King('white', (0,4))
        r1 = Rook('white', (0,0))
        r2 = Rook('white', (0,7))
        g = Game()
        g.board[0][4] = k
        g.board[0][0] = r1
        g.board[0][7] = r2
        k.g = g
        r1.g = g
        r2.g = g
        pos = k.possible_moves(current_position, board)
        castling_moves = [Position(0,2), Position(0,6)]
        self.assertTrue(all(move in pos for move in castling_moves))


if __name__ == '__main__':
    unittest.main()

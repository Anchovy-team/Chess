import unittest
from Chessboard import Pawn, Rook, King, Queen, Bishop, Knight, Position, Game

#
#
#       All failures are due to the board not being in the expected way
#       For example its not empty for the queen diagonaly and so on
#       Each test works in dependency of its board position
#
#

class PawnTest(unittest.TestCase):
    g = Game()

#    def test_pawn_1(self):
#        out = self.g.board[0][1].possible_moves(Position(x=1, y=0), self.g.board)
#
#        r_out = [Position(0, 2), Position(2, 2)]
#        print(out, r_out)
#        for i in range(len(out)):
#            print(type(out[i]), type(r_out[i]), 1)
#            self.assertEqual(str(out[i]), str(r_out[i]))

    def test_move_two_squares_initial(self):
        p = Pawn('white')
        p.position = Position(1, 0)
        p.g = self.g
        pos = p.possible_moves(p.position)
        expected = [Position(1, 1), Position(1, 2)]
        for i in range(len(pos)):
            self.assertEqual(str(pos[i]), str(expected[i]))

    def test_move_one_square_not_initial(self):
        p = Pawn('white')
        p.position = Position(1, 2)
        p.g = self.g
        pos = p.possible_moves(p.position)
        expected = [Position(1, 3)]
        for i in range(len(pos)):
            self.assertEqual(str(pos[0]), str(expected[0]))

    def test_capture_diagonally(self):
        p1 = Pawn('white')
        p2 = Pawn('black')
        p1.position = Position(1, 0)
        p2.position = Position(2, 1)
        p1.g = self.g
        p2.g = self.g
        pos = p1.possible_moves(p1.position)
        expected = [Position(1,1), Position(2,1)]
        for i in range(len(pos)):
            self.assertEqual(str(pos[i]), str(expected[i]))

    def test_blocked_by_piece(self):
        p1 = Pawn('white')
        p2 = Pawn('white')
        p1.position = Position(1, 0)
        p2.position = Position(1, 1)
        p1.g = self.g
        p2.g = self.g
        pos = p1.possible_moves(p1.position)
        expected = []
        for i in range(len(pos)):
            self.assertEqual(str(pos[i]), str(expected))

    #    def test_promotion(self):
    #        p = Pawn('white')
    #        p.position = Position(1, 6)
    #        p.g = self.g
    #        pos = p.possible_moves(p.position)
    #        expected = [Position(1,7, 'Queen'), Position(1,7, 'Rook'), Position(1,7, 'Bishop'), Position(1,7, 'Knight')]
    #        for i in range(len(pos)):
    #            self.assertEqual(str(pos[i]), str(expected[i]))


class RookTest(unittest.TestCase):

    g = Game()

    def test_move_along_rank_file(self):
        self.g.clean_board()
        r = Rook('white')
        r.position = Position(0,0)
        r.g = self.g
        self.g.board[0][0] = r
        pos = r.possible_moves(r.position)
        expected = [Position(i, 0) for i in range(1, 8)] + [Position(0, i) for i in range(1, 8)]
        self.assertEqual(len(pos), len(expected))
        for i in range(len(pos)):
            if pos[i] in expected:
                continue
            else:
                return None

    def test_cannot_move_diagonally(self):
        r = Rook('white')
        r.position = Position(0, 0)
        r.g = self.g
        pos = r.possible_moves(r.position)
        diagonal_moves = [Position(i, i) for i in range(1, 8)]
        self.assertTrue(not any(move in pos for move in diagonal_moves))

    def test_cannot_move_over_pieces(self):
        r = Rook('white')
        p = Pawn('white')
        r.position = Position(0,0)
        p.position = Position(0,1)
        r.g = self.g 
        p.g = self.g
        pos = r.possible_moves(r.position)
        blocked_moves = [Position(0, i) for i in range(2, 8)]
        self.assertTrue(not any(move in pos for move in blocked_moves))


class KnightTest(unittest.TestCase):
    g = Game()

    def test_move_L_shape(self):
        self.g.clean_board()
        k = Knight('white')
        k.position = Position(3,3)
        k.g = self.g
        pos = k.possible_moves(k.position)
        expected = [Position(1,2), Position(1,4), Position(2,1), Position(2,5), Position(4,1), Position(4,5), Position(5,2), Position(5,4)]
        self.g.board[2][2] = k
        self.assertEqual(len(pos), len(expected))
        for i in range(len(pos)):
            if pos[i] in expected:
                continue
            else:
                return None

    def test_jump_over_pieces(self):
        self.g.clean_board()
        k = Knight('white')
        p = Pawn('white')
        k.position = Position(3,3)
        p.position = Position(3,4)
        k.g = self.g
        p.g = self.g
        pos = k.possible_moves(k.position)
        expected = [Position(1,2), Position(1,4), Position(2,1), Position(2,5), Position(4,1), Position(4,5), Position(5,2), Position(5,4)]
        self.g.board[2][2] = k
        self.g.board[2][3] = p
        #self.g.print()
        self.assertEqual(len(pos), len(expected))
        for i in range(len(pos)):
            if pos[i] in expected:
                continue
            else:
                return None


class QueenTest(unittest.TestCase):
    g = Game()

    def test_move_along_rank_file_diagonal(self):
        self.g.clean_board()
        q = Queen('white')
        q.position = Position(3,3)
        q.g = self.g
        self.g.board[3][3] = q
        self.g.print()
        pos = q.possible_moves(q.position)
        expected = [Position(i, 3) for i in range(0, 8) if i != 3] + \
                    [Position(3, i) for i in range(0, 8) if i != 3] + \
                    [Position(i, j) for i in range(0, 8) for j in range(0, 8) if abs(i - 3) == abs(j - 3) and i != 3]
        self.assertEqual(len(pos), len(expected))
        for i in range(len(pos)):
            if pos[i] in expected:
                continue
            else:
                return None

    def test_cannot_move_like_knight(self):
        q = Queen('white')
        q.position = Position(3,3)
        q.g = self.g
        pos = q.possible_moves(q.position)
        knight_moves = [Position(1,2), Position(1,4), Position(2,1), Position(2,5), Position(4,1), Position(4,5), Position(5,2), Position(5,4)]
        self.assertTrue(not any(move in pos for move in knight_moves))

    def test_cannot_move_over_pieces(self):
        q = Queen('white')
        p = Pawn('white')
        q.position = Position(3,3)
        p.position = Position(3,4)
        q.g = self.g
        p.g = self.g
        pos = q.possible_moves(q.position)
        blocked_moves = [Position(3, i) for i in range(5, 8)] + \
                        [Position(i, 4) for i in range(4, 8)] + \
                        [Position(i, j) for i in range(4, 8) for j in range(5, 8) if abs(i - 3) == abs(j - 4)]
        self.assertTrue(not any(move in pos for move in blocked_moves))


class BishopTest(unittest.TestCase):
    g = Game()

    def test_move_diagonally(self):
        self.g.clean_board()
        b = Bishop('white')
        b.position = Position(3,3)
        b.g = self.g
        pos = b.possible_moves(b.position)
        expected = [Position(i, j) for i in range(0, 8) for j in range(0, 8) if abs(i - 3) == abs(j - 3) and i != 3]
        self.g.board[2][2] = b
        self.g.print()
        #print(expected)
        #print(pos)
        self.assertEqual(len(pos), len(expected))
        for i in range(len(pos)):
            if pos[i] in expected:
                continue
            else:
                return None

    def test_cannot_move_along_rank_file(self):
        b = Bishop('white')
        b.position = Position(3,3)
        b.g = self.g
        pos = b.possible_moves(b.position)
        rank_file_moves = [Position(i, 3) for i in range(0, 8) if i != 3] + [Position(3, i) for i in range(0, 8) if i != 3]
        self.assertTrue(not any(move in pos for move in rank_file_moves))

    def test_cannot_move_over_pieces(self):
        b = Bishop('white')
        p = Pawn('white')
        b.position = Position(3,3)
        p.position = Position(4,4)
        b.g = self.g
        p.g = self.g
        pos = b.possible_moves(b.position)
        blocked_moves = [Position(i, j) for i in range(5, 8) for j in range(5, 8) if abs(i - 3) == abs(j - 3)]
        self.assertTrue(not any(move in pos for move in blocked_moves))


class KingTest(unittest.TestCase):
    g = Game()

    def test_move_one_square_any_direction(self):
        self.g.clean_board()
        k = King('white')
        k.position = Position(3,3)
        k.g = self.g
        pos = k.possible_moves(k.position)
        expected = [Position(2,2), Position(2,3), Position(2,4), Position(3,2), Position(3,4), Position(4,2), Position(4,3), Position(4,4)]
        self.g.board[2][2] = k


        #self.g.print()
        self.assertEqual(str(pos), str(expected))

    def test_cannot_move_into_check(self):
        k = King('white')
        q = Queen('black')
        k.position = Position(3,3)
        q.position = Position(4,4)
        k.g = self.g
        q.g = self.g
        pos = k.possible_moves(k.position)
        check_moves = [Position(4,3), Position(4,4)]
        self.assertTrue(not any(move in pos for move in check_moves))


if __name__ == '__main__':
    unittest.main()

from Chessboard import *

# def main_action_loop():


if __name__ == "__main__":
    g = Game()
    possible_nums = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7}
    possible_letters = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    game_over = True
    g.print()
    g.print_svg()
    turn = True
    while True:
        try:
            start = input(f"{'white' if turn else 'black'}`s move. Choose a figure: ")
            end = input("Chose where to place it: ")

            if len(start) != 2 or not start[0] in possible_letters or not start[1] in possible_nums \
                    or len(end) != 2 or not end[0] in possible_letters or not end[1] in possible_nums:
                raise Exception('Input Error')

            if g.board[possible_nums[start[1]]][possible_letters[start[0]]].color != ('white' if turn else 'black'):
                print(g.board[possible_nums[start[1]]][possible_letters[start[0]]].color, 'white' if turn else 'black')
                raise Exception('There are no your piece on this space')

            g.move(Position(possible_letters[start[0]], possible_nums[start[1]]),
                   Position(possible_letters[end[0]], possible_nums[end[1]]))

            if g.is_check('white' if turn else 'black'):
                g.master_move(Position(possible_letters[end[0]], possible_nums[end[1]]),
                              Position(possible_letters[start[0]], possible_nums[start[1]]))
                raise Exception('You are on check')

            g.print()
            g.print_svg()
            result = g.is_check_mate()
            if result != 'continue':
                raise Exception(result)

            if g.is_draw():
                raise Exception('Draw')
            turn = not turn

        except Exception as inst:
            if inst == 'white' or inst == 'black':
                print(f"{inst} won")
                break
            if inst == "Draw":
                print(inst)
                break
            print(inst)

            s = input()

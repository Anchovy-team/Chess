from Chessboard import *

if __name__ == "__main__":

    g = Game()
    possible_nums = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7}
    possible_letters = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    game_over = True
    g.print()
    while game_over:

        for turn in ["white", "black"]:
            while True:
                start = input(f"{turn}`s move. Choose a figure: ")
                end = input("Chose where to place it: ")
                if len(start) > 2 or not start[0] in possible_letters or not start[1] in possible_nums \
                        or len(end) > 2 or not end[0] in possible_letters or not end[1] in possible_nums:
                    print('Input error')
                    g.print()
                    continue
                if g.board[possible_nums[start[1]]][possible_letters[start[0]]].color != turn:
                    print("There are no your piece on this space")
                    g.print()
                    continue
                if g.move(Position(possible_letters[start[0]], possible_nums[start[1]]),
                       Position(possible_letters[end[0]], possible_nums[end[1]])) == False:
                    continue
                if g.is_check(turn):
                    print("You are on check")
                    g.master_move(Position(possible_letters[end[0]], possible_nums[end[1]]),\
                                  Position(possible_letters[start[0]], possible_nums[start[1]]))
                    g.print()
                    continue
                else:
                    g.print()
                    break
            if g.is_check_mate() != 'continue':
                g.game_over = False
                print(g.is_check_mate(), "lost")
                break
            elif g.is_draw():
                print("DRAW")
                g.game_over = False





            # input module
            #start = input("Choose a figure: ")
            #end = input("Chose where to place it: ")
            #if len(start) > 2 or not start[0] in possible_letters or not start[1] in possible_nums \
            #       or len(end) > 2 or not end[0] in possible_letters or not end[1] in possible_nums:
            #    raise Exception('Input Error')

            #g.move(Position(possible_letters[start[0]], possible_nums[start[1]]),
            #       Position(possible_letters[end[0]], possible_nums[end[1]]))

            #if g.is_check_mate() != 'continue':
            #    g.print()
            #    if g.is_check_mate() == 'white':
            #        raise Exception('Black won, game finished')
            #    elif g.is_check_mate() == 'black':
            #        raise Exception('White won, game finished')

            #if g.is_draw():
            #    g.print()
            #    raise Exception('Draw, game finished')

            #if g.is_check('black'):
            #      FIXME
            #    pass

            #if g.is_check('white'):
                # FIXME
            #    pass

            # output module
            #g.print()

        #except Exception as inst:
        #    print(inst)
        #    s = input()

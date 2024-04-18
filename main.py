from Chessboard import *

if __name__ == "__main__":

    g = Game()
    possible_nums = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7}
    possible_letters = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    g.print()

    while True:
        try:
            # input module
            start = input("Choose a figure: ")
            end = input("Chose where to place it: ")
            if len(start) > 2 or not start[0] in possible_letters or not start[1] in possible_nums \
                    or len(end) > 2 or not end[0] in possible_letters or not end[1] in possible_nums:
                raise Exception('Input Error')
            else:
                g.move(Position(possible_letters[start[0]], possible_nums[start[1]]),
                       Position(possible_letters[end[0]], possible_nums[end[1]]))
                g.print()

            if g.is_check_mate():
                raise Exception('Game finished')

            # output module
            print(possible_letters[start[0]], possible_nums[start[1]])
            print(possible_letters[end[0]], possible_nums[end[1]])
            g.print()
        except Exception as inst:
            print(inst)
            s = input()

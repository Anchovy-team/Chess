from Chessboard import *

if __name__ == "__main__":
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

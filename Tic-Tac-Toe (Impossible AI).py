import os
os.system('cls')

def Game_Loop():

    Input1 = ("1")
    Input2 = ("2")
    Input3 = ("3")
    Input4 = ("4")
    Input5 = ("5")
    Input6 = ("6")
    Input7 = ("7")
    Input8 = ("8")
    Input9 = ("9")
    Input0 = ("1")

    Game_Running = True

    print("Here Is Your Board:" "\n")
    print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
    OInput = input("Type whatever number on the board you want to put an O and then the AI will immediately respond: ")

    def AI(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9, Input0):

        if Input5 == "5":
            return "X", 5
        if Input1 == "O" and Input2 == "O" and Input3 == "3":
            return "X", 3
        if Input4 == "O" and Input5 == "O" and Input6 == "6":
            return "X", 6
        if Input7 == "O" and Input8 == "O" and Input9 == "9":
            return "X", 9
        if Input9 == "O" and Input8 == "O" and Input7 == "7":
            return "X", 7
        if Input6 == "O" and Input5 == "O" and Input4 == "4":
            return "X", 4
        if Input3 == "O" and Input2 == "O" and Input1 == "1":
            return "X", 1
        if Input1 == "O" and Input4 == "O" and Input7 == "7":
            return "X", 7
        if Input2 == "O" and Input5 == "O" and Input8 == "8":
            return "X", 8
        if Input3 == "O" and Input6 == "O" and Input9 == "9":
            return "X", 9
        if Input9 == "O" and Input6 == "O" and Input3 == "3":
            return "X", 3
        if Input8 == "O" and Input5 == "O" and Input2 == "2":
            return "X", 2
        if Input7 == "O" and Input4 == "O" and Input1 == "1":
            return "X", 1
        if Input1 == "O" and Input3 == "O" and Input2 == "2":
            return "X", 2
        if Input4 == "O" and Input6 == "O" and Input5 == "5":
            return "X", 5
        if Input7 == "O" and Input9 == "O" and Input8 == "8":
            return "X", 8
        if Input1 == "O" and Input7 == "O" and Input4 == "4":
            return "X", 4
        if Input2 == "O" and Input8 == "O" and Input5 == "5":
            return "X", 5
        if Input3 == "O" and Input9 == "O" and Input6 == "6":
            return "X", 6
        if Input1 == "O" and Input5 == "O" and Input9 == "9":
            return "X", 9
        if Input9 == "O" and Input5 == "O" and Input1 == "1":
            return "X", 1
        if Input3 == "O" and Input5 == "O" and Input7 == "7":
            return "X", 7
        if Input7 == "O" and Input5 == "O" and Input3 == "3":
            return "X", 3
        if Input3 == "O" and Input7 == "O" and Input5 == "5":
            return "X", 5
        if Input1 == "O" and Input9 == "O" and Input5 == "5":
            return "X", 5
        if Input1 == "O" and Input9 == "O" and Input2 == "2":
            return "X", 2
        if Input3 == "O" and Input7 == "O" and Input2 == "2":
            return "X", 2
        if Input4 == "O" and Input8 == "O" and Input7 == "7":
            return "X", 7
        if Input4 == "O" and Input2 == "O" and Input1 == "1":
            return "X", 1
        if Input6 == "O" and Input2 == "O" and Input3 == "3":
            return "X", 3
        if Input6 == "O" and Input8 == "O" and Input9 == "9":
            return "X", 9
        if Input3 == "O" and Input8 == "O" and Input9 == "9":
            return "X", 9
        if Input1 == "O" and Input8 == "O" and Input7 == "7":
            return "X", 7
        if Input2 == "O" and Input9 == "O" and Input3 == "3":
            return "X", 3
        if Input5 == "O" and Input9 == "O" and Input3 == "3":
            return "X", 3
        if Input1 == "X" and Input2 == "X" and Input3 == "3":
            return "X", 3
        if Input4 == "X" and Input5 == "X" and Input6 == "6":
            return "X", 6
        if Input7 == "X" and Input8 == "X" and Input9 == "9":
            return "X", 9
        if Input1 == "X" and Input4 == "X" and Input7 == "7":
            return "X", 7
        if Input2 == "X" and Input5 == "X" and Input8 == "8":
            return "X", 8
        if Input3 == "X" and Input6 == "X" and Input9 == "9":
            return "X", 9
        if Input1 == "X" and Input5 == "X" and Input9 == "9":
            return "X", 9
        if Input9 == "X" and Input5 == "X" and Input1 == "1":
            return "X", 1
        if Input3 == "X" and Input5 == "X" and Input7 == "7":
            return "X", 7
        if Input3 == "X" and Input7 == "X" and Input5 == "5":
            return "X", 5
        if Input1 == "X" and Input9 == "X" and Input5 == "5":
            return "X", 5
        if Input1 == "X" and Input3 == "X" and Input2 == "2":
            return "X", 2
        if Input4 == "X" and Input6 == "X" and Input5 == "5":
            return "X", 5
        if Input7 == "X" and Input9 == "X" and Input8 == "8":
            return "X", 8
        if Input1 == "X" and Input7 == "X" and Input4 == "4":
            return "X", 4
        if Input2 == "X" and Input8 == "X" and Input5 == "5":
            return "X", 5
        if Input3 == "X" and Input9 == "X" and Input6 == "6":
            return "X", 6
        if Input5 == "X" and Input2 == "X" and Input3 == "3" and Input7 == "7" and Input8 == "8":
            return "X", 3
        if Input1 == "X" and Input9 == "X" and Input7 == "7":
            return "X", 7
        if Input1 == "X" and Input9 == "X" and Input3 == "3":
            return "X", 3
        if Input3 == "X" and Input7 == "X" and Input1 == "1":
            return "X", 1
        if Input3 == "X" and Input7 == "X" and Input9 == "9":
            return "X", 9
        if all(pos in ["O", "X"] for pos in [Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9]):
            return "X", 0
        else:
            for i, pos in enumerate([Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9], 1):
                if pos == str(i):
                    return "X", i

    def Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9):

        if Input1 == "O" and Input2 == "O" and Input3 == "O":
            print("Here Is Your Board:" "\n")
            print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
            print("Player Wins!")
            exit()
        elif Input4 == "O" and Input5 == "O" and Input6 == "O":
            print("Here Is Your Board:" "\n")
            print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
            print("Player Wins!")
            exit()
        elif Input7 == "O" and Input8 == "O" and Input9 == "O":
            print("Here Is Your Board:" "\n")
            print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
            print("Player Wins!")
            exit()
        elif Input1 == "O" and Input4 == "O" and Input7 == "O":
            print("Here Is Your Board:" "\n")
            print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
            print("Player Wins!")
            exit()
        elif Input2 == "O" and Input5 == "O" and Input8 == "O":
            print("Here Is Your Board:" "\n")
            print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
            print("Player Wins!")
            exit()
        elif Input3 == "O" and Input6 == "O" and Input9 == "O":
            print("Here Is Your Board:" "\n")
            print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
            print("Player Wins!")
            exit()
        elif Input1 == "O" and Input5 == "O" and Input9 == "O":
            print("Here Is Your Board:" "\n")
            print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
            print("Player Wins!")
            exit()
        elif Input3 == "O" and Input5 == "O" and Input7 == "O":
            print("Here Is Your Board:" "\n")
            print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
            print("Player Wins!")
            exit()

    def AI_Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9):

        if Input1 == "X" and Input2 == "X" and Input3 == "X":
            print("AI Wins!")
            exit()
        elif Input4 == "X" and Input5 == "X" and Input6 == "X":
            print("AI Wins!")
            exit()
        elif Input7 == "X" and Input8 == "X" and Input9 == "X":
            print("AI Wins!")
            exit()
        elif Input1 == "X" and Input4 == "X" and Input7 == "X":
            print("AI Wins!")
            exit()
        elif Input2 == "X" and Input5 == "X" and Input8 == "X":
            print("AI Wins!")
            exit()
        elif Input3 == "X" and Input6 == "X" and Input9 == "X":
            print("AI Wins!")
            exit()
        elif Input1 == "X" and Input5 == "X" and Input9 == "X":
            print("AI Wins!")
            exit()
        elif Input3 == "X" and Input5 == "X" and Input7 == "X":
            print("AI Wins!")
            exit()
        elif all(pos in ["O", "X"] for pos in [Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9]):
            print("Draw.")
            exit()

    while Game_Running:
        if OInput == "1" and Input1 == "1":
            os.system('cls')
            Input1 = ("O")
            Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
            value, pos = AI(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9, Input0)
            if pos == 1: Input1 = value
            elif pos == 2: Input2 = value
            elif pos == 3: Input3 = value
            elif pos == 4: Input4 = value
            elif pos == 5: Input5 = value
            elif pos == 6: Input6 = value
            elif pos == 7: Input7 = value
            elif pos == 8: Input8 = value
            elif pos == 9: Input9 = value
            elif pos == 0: Input0 = value
            print("Here Is Your Board:" "\n")
            print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
            
            AI_Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
            OInput = input("New Input: ")
        else:
            if OInput == "2" and Input2 == "2":
                os.system('cls')
                Input2 = ("O")
                Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                value, pos = AI(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9, Input0)
                if pos == 1: Input1 = value
                elif pos == 2: Input2 = value
                elif pos == 3: Input3 = value
                elif pos == 4: Input4 = value
                elif pos == 5: Input5 = value
                elif pos == 6: Input6 = value
                elif pos == 7: Input7 = value
                elif pos == 8: Input8 = value
                elif pos == 9: Input9 = value
                elif pos == 0: Input0 = value
                print("Here Is Your Board:" "\n")
                print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
                
                AI_Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                OInput = input("New Input: ")
            else:
                if OInput == "3" and Input3 == "3":
                    os.system('cls')
                    Input3 = ("O")
                    Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                    value, pos = AI(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9, Input0)
                    if pos == 1: Input1 = value
                    elif pos == 2: Input2 = value
                    elif pos == 3: Input3 = value
                    elif pos == 4: Input4 = value
                    elif pos == 5: Input5 = value
                    elif pos == 6: Input6 = value
                    elif pos == 7: Input7 = value
                    elif pos == 8: Input8 = value
                    elif pos == 9: Input9 = value
                    elif pos == 0: Input0 = value
                    print("Here Is Your Board:" "\n")
                    print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
                    AI_Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                    OInput = input("New Input: ")
                else:
                    if OInput == "4" and Input4 == "4":
                        os.system('cls')
                        Input4 = ("O")
                        Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                        value, pos = AI(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9, Input0)
                        if pos == 1: Input1 = value
                        elif pos == 2: Input2 = value
                        elif pos == 3: Input3 = value
                        elif pos == 4: Input4 = value
                        elif pos == 5: Input5 = value
                        elif pos == 6: Input6 = value
                        elif pos == 7: Input7 = value
                        elif pos == 8: Input8 = value
                        elif pos == 9: Input9 = value
                        elif pos == 0: Input0 = value
                        print("Here Is Your Board:" "\n")
                        print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
                        AI_Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                        OInput = input("New Input: ")
                    else:
                        if OInput == "5" and Input5 == "5":
                            os.system('cls')
                            Input5 = ("O")
                            Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                            value, pos = AI(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9, Input0)
                            if pos == 1: Input1 = value
                            elif pos == 2: Input2 = value
                            elif pos == 3: Input3 = value
                            elif pos == 4: Input4 = value
                            elif pos == 5: Input5 = value
                            elif pos == 6: Input6 = value
                            elif pos == 7: Input7 = value
                            elif pos == 8: Input8 = value
                            elif pos == 9: Input9 = value
                            elif pos == 0: Input0 = value
                            print("Here Is Your Board:" "\n")
                            print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
                            AI_Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                            OInput = input("New Input: ")
                        else:
                            if OInput == "6" and Input6 == "6":
                                os.system('cls')
                                Input6 = ("O")
                                Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                                value, pos = AI(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9, Input0)
                                if pos == 1: Input1 = value
                                elif pos == 2: Input2 = value
                                elif pos == 3: Input3 = value
                                elif pos == 4: Input4 = value
                                elif pos == 5: Input5 = value
                                elif pos == 6: Input6 = value
                                elif pos == 7: Input7 = value
                                elif pos == 8: Input8 = value
                                elif pos == 9: Input9 = value
                                elif pos == 0: Input0 = value
                                print("Here Is Your Board:" "\n")
                                print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
                                AI_Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                                OInput = input("New Input: ")
                            else:
                                if OInput == "7" and Input7 == "7":
                                    os.system('cls')
                                    Input7 = ("O")
                                    Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                                    value, pos = AI(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9, Input0)
                                    if pos == 1: Input1 = value
                                    elif pos == 2: Input2 = value
                                    elif pos == 3: Input3 = value
                                    elif pos == 4: Input4 = value
                                    elif pos == 5: Input5 = value
                                    elif pos == 6: Input6 = value
                                    elif pos == 7: Input7 = value
                                    elif pos == 8: Input8 = value
                                    elif pos == 9: Input9 = value
                                    elif pos == 0: Input0 = value
                                    print("Here Is Your Board:" "\n")
                                    print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
                                    AI_Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                                    OInput = input("New Input: ")
                                else:
                                    if OInput == "8" and Input8 == "8":
                                        os.system('cls')
                                        Input8 = ("O")
                                        Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                                        value, pos = AI(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9, Input0)
                                        if pos == 1: Input1 = value
                                        elif pos == 2: Input2 = value
                                        elif pos == 3: Input3 = value
                                        elif pos == 4: Input4 = value
                                        elif pos == 5: Input5 = value
                                        elif pos == 6: Input6 = value
                                        elif pos == 7: Input7 = value
                                        elif pos == 8: Input8 = value
                                        elif pos == 9: Input9 = value
                                        elif pos == 0: Input0 = value
                                        print("Here Is Your Board:" "\n")
                                        print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
                                        AI_Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                                        OInput = input("New Input: ")
                                    else:
                                        if OInput == "9" and Input9 == "9":
                                            os.system('cls')
                                            Input9 = ("O")
                                            Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                                            value, pos = AI(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9, Input0)
                                            if pos == 1: Input1 = value
                                            elif pos == 2: Input2 = value
                                            elif pos == 3: Input3 = value
                                            elif pos == 4: Input4 = value
                                            elif pos == 5: Input5 = value
                                            elif pos == 6: Input6 = value
                                            elif pos == 7: Input7 = value
                                            elif pos == 8: Input8 = value
                                            elif pos == 9: Input9 = value
                                            elif pos == 0: Input0 = value
                                            print("Here Is Your Board:" "\n")
                                            print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
                                            AI_Win_Check(Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9)
                                            OInput = input("New Input: ")
                                        else:
                                            if OInput == " ":
                                                os.system('cls')
                                                print("Here Is Your Board:" "\n")
                                                print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
                                                OInput = input("New Input: ")
                                            else:
                                                if OInput == "":
                                                    os.system('cls')
                                                    print("Here Is Your Board:" "\n")
                                                    print("\x1B[4m" + f"{Input1}|{Input2}|{Input3}" "\n" f"{Input4}|{Input5}|{Input6}" "\n" + "\x1B[0m" + f"{Input7}|{Input8}|{Input9}" "\n")
                                                    OInput = input("New Input: ")
                                        
Game_Loop()
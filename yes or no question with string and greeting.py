#Copyright 2022 Mitchell E Wise
#SPDX-License-Identifier: Apache-2.0
    
        
eng = {
    "a": " = ",
    "b": 'input("',
    "c": '")',
    "d": "while True:",
    "e": "    ",
    "f": "        ",
    "g": "if ",
    "h": " == ",
    "i": ":",
    "j": "elif ",
    "k": "else:",
    "l": "break",
    "m": '"',
    "n": 'print("',
    "o": " "
}
print("#Select s for single line string.")
print("#Select g for greeting.")
print("#select y for yes or no question.")
while True:
    print("#Select s, g, or y. Select x to exit m for main.")
        
    switch = input("#")
    if switch ==  "s":
        while True:
            print("#Enter text. This is after print function.")
            text = input("#")
            if text == "m":
                break
            print('print("' + text + '")\n')
    elif switch == "g":
        print("#This is one step above the single line string.")
        print("#The greeting is 2 lines of code. It uses a variable and input function")
        while True:
            print("#Name the variable.")
            n = input("#")
            if n == "m":
                break
            print("#Ask question. What is your name would be appropriate.")
            print("#This is assigning a value to the variable.")
            print("#The input function is used for user input.")
            print("#The users input will be assighned to the variable.")
            q = input("#")
            print(n + ' = input("' + q + ' ")')
            print('print("Hi "' + "+ " + n + ")\n")
    elif switch == "y":
        while True:
            print("#The leters correspond with the components of the yes or no question.")
            print("#The letters must be entered in the proper order to continue.")
            print("#The while loop and break statments are so the program will repeat if the user typed something wrong.")
            print("#Enter s to skip questions m to exit.\n")
            print('''
                     #a - break
                     #b - elif
                     #c - else
                     #d - if statment
                     #e - variable and question in one line.
                     #f - while loop\n ''')
            print("#Enter letters in proper order.")
            letters = input("#")
            if letters.lower() == "f" + "e" + "d"+ "a" +"b" + "a"+ "c":
                print("#Right choice.")
            elif letters == "s":
                pass
            elif letters == "m":
                break
            else:
                continue
            print("#Use this to ask a yes or no question in python without writing any code.\n")
            print("#Enter m for main. Press enter to continue. ")
            ex = input("#")
            if ex == "m":
                break
            print("#Name the variable.")
            v = input("#")
            print("#Ask the question then press enter.")
            a = input("#")
            print("#Enter yes or no to the if statment.")
            i = input("#")
            print("#Enter a one line answer if yes or no.")
            e = input("#")
            print("#Enter no if last was yes or visa versa to elif.")
            el = input("#")
            print("#Enter a one line answer.")
            el1 = input("#")
            print("#Enter answer if neither yes or no is chosen to else.")
            els = input("#")
            print(eng["d"])
            print(eng["e"] + v + eng["a"] + eng["b"] + a + eng["o"] + eng["c"])
            print(eng["e"] + eng["g"] + v + eng["h"] +eng["m"] + i + eng["m"] +  eng["i"] )
            print(eng["f"] + eng["n"] + e + eng["c"])
            print(eng["f"] + eng["l"])
            print(eng["e"] + eng["j"] + v + eng["h"] +eng["m"] + el + eng["m"] +  eng["i"] )
            print(eng["f"] + eng["n"] + el1 + eng["c"])
            print(eng["f"] + eng["l"])
            print(eng["e"] + eng["k"])
            print(eng["f"] + eng["n"] + els + eng["c"])
    elif switch == "x":
        break




















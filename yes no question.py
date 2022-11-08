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
while True:
    print("#The leters correspond with the components of the yes or no question.")
    print("#The letters must be entered in the proper order to continue.")
    print("#The while loop and break statments are so the program will repeat if the user typed something wrong.")
    print("#Enter m to skip questions x to exit.\n")
    print('''
             #a - break
             #b - elif
             #c - else
             #d - if statment
             #e - variable and question in one line.
             #f - while loop\n ''')
    print("#Enter letters in proper order.")
    letters = input()
    if letters.lower() == "f" + "e" + "d"+ "a" +"b" + "a"+ "c":
        print("#Right choice.")
    elif letters == "m":
        pass
    elif letters == "x":
        break
    else:
        continue
    print("#Use this to ask a yes or no question in python without writing any code.\n")
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

    
    

    
        
    
    


            

        


                   

                
      
            

       
      

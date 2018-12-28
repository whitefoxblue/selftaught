def hangman(word): # function 'hangman' takes param 'word' 
    wrong = 0 # how many incorrect letters player has gussed
    stages = ["", # list of strings used to draw hangman, printed one at a time 
              " ______       ",
              "|             ",
              "|       |     ",
              "|       0     ",
              "|      /|\    ",
              "|      / \    ",
              "|             "
               ]

    rletters = list(word) # list containing each character in variable 'word' left to guess
    board = ["__"] * len(word) # list of '__' strings to give hit of letters left to guess
    win = False # keeps track of if player won game yet, 'False' when hasn't won yet
    print("Welcome to Hangman")
    print("word:", word) #
    print("wrong:",wrong) #
    print("rletters:", rletters) #
    print("board:",board) #
    while wrong < len(stages): # loop continues as long as wrong guesses < stages 
        print("\n") # print blank space
        # msg = "Guess a letter " 
        char = input("Guess a letter: ")  # char = input(msg)
        if char in rletters: # if player guesses a letter correctly that hasn't been guessed
            cind = rletters \
                   .index(char) # sets variable 'cind' to the index in 'rletters' var 'cind' is at
            print("cind", cind) #
            board[cind] = char # set 'board' list at 'cind' which is index for 'char' to 'char'
            print("board[cind]", board[cind]) #
            rletters[cind] = '$' # set 'rletters' list at 'cind' which is index for 'char' to 'char' 
            print("rletters[cind]", rletters[cind]) #
            print("rletters:", rletters)#
        else:
            wrong += 1 # increment wrong ++ for wrong answer
        print(" ".join(board)) # prints board list items seperated by spaces; current correct 
        print('"_".join(board)^')#
        e = wrong + 1 # set length of 'stages' list to print to one more than value of variable 'wrong'
        print("e: ", e) #
        print("\n"
              .join(stages[0: e])) # prints hangman so far
        print("join(stages[0: e]^") #
        if "__" not in board:
            print("You win!")
            print(" ".join(board)) # prints board w/filled in letters
            print('" ".joint(board)^')#
            win = True
            break # ends the program
    if not win: # 'win' = False so i.e. 'if True'
        print("\n"
               .join(stages[0: \
                wrong]))
        print(".join(stages[0:wrong]^")
        print("You lose! It was {}."
                  .format(word))

hangman("cattle")

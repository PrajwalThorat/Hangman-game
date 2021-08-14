import random

def hangman():
    word = random.choice(["superman","batman","hangman","ironman","spiderman","thor","deadpool","hulk","antman"])
    validletter = 'abcdefghijklmnopqrstuvwxyz'
    turn = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0
        
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You Win!")
            break

        
        print("guess the word :", main)
        guess = input()
        
        if guess in validletter:
            guessmade = guessmade + guess
        else:
            print("Enter the valid character")
            guess = input()

            
        if guess not in word:
            turn = turn - 1
            if turn == 9:
                print("9 turn are left")
                print(" -------------- ")
            if turn == 8:
                print("8 turn are left")
                print(" -------------- ")
                print("       O        ")
            if turn == 7:
                print("7 turn are left")
                print(" -------------- ")
                print("       O        ")
                print("       |        ")
            if turn == 6:
                print("6 turn are left")
                print(" -------------- ")
                print("       O        ")
                print("       |        ")
                print("      /         ")
            if turn == 5:
                print("5 turn are left")
                print(" -------------- ")
                print("       O        ")
                print("       |        ")
                print("      / \       ")
            if turn == 4:
                print("4 turn are left")
                print(" -------------- ")
                print("     \ O        ")
                print("       |        ")
                print("      / \       ")
            if turn == 3:
                print("3 turn are left")
                print(" -------------- ")
                print("     \ O /      ")
                print("       |        ")
                print("      / \       ")
            if turn == 2:
                print("2 turn are left")
                print(" -------------- ")
                print("     \ O /|     ")
                print("       |        ")
                print("      / \       ")
            if turn == 1:
                print("1 turn are left")
                print("last breath counting , take care")
                print(" -------------- ")
                print("      \O_|     ")
                print("       |\       ")
                print("      / \       ")
            if turn == 0:
                print("You loose")
                print("you let a kind man die ")
                print(" -------------- ")
                print("       O_|      ")
                print("      /|\       ")
                print("      / \       ")
                break
      






name = input("Enter your name:")

print("Welcome" , name)
print("-----------------------")

print("Try to find out Super-Hero names ")
print("Try to guess the word in less than 10 attempt")

hangman()
print()



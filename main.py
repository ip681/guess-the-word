import random
from termcolor import colored

words = ['cat', 'computer', 'coffee']
man = ["________ \n| \n| \n| \n| \n| \n| \n|____________",
       "________ \n|      | \n| \n| \n| \n| \n| \n|____________",
       "________ \n|      | \n|      O \n| \n| \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|      | \n| \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|      | \n|      | \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|     /| \n|      | \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|     /| \n|    / | \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|     /|\\ \n|    / | \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|     /|\\ \n|    / | \\ \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|     /|\\ \n|    / | \\ \n|     / \n| \n|____________",
       "________ \n|      | \n|      O \n|     /|\\ \n|    / | \\ \n|     / \n|    / \n|____________",
       "________ \n|      | \n|      O \n|     /|\\ \n|    / | \\ \n|     / \\ \n|    / \n|____________",
       "________ \n|      | \n|      O \n|     /|\\ \n|    / | \\ \n|     / \\ \n|    /   \\ \n|____________"]

word = random.choice(words)
guesses = ""
wrong_guesses = ""
MAX_TURNS = 12
turns = 12

print("Guess the word")
while turns > 0:

    print("____________________________________________________________________\n")
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print("") # new line
    if failed == 0:
        print(colored("You Win!", "green"))
        print(f"The word is: {word}")
        break

    print()

    while True:

        guess = input("Input letter: ")

        # if guesses.find(str(guess)) != -1:
        #     print(f"You already try the letter {guess}")
        #     turns += 1

        if len(guess) == 1 and guess.isalpha(): # check for more than one character and not letter character
            guess = guess.lower() # make the letter lowercase if it is uppercase
            break
        else:
            print("Enter a single letter (a-z).")
            continue

    guesses += guess

    if guess not in word: #checks if the letter entered is part of a word
        turns -= 1
        print(f"Wrong! You have {turns} more guesses")
        wrong_guesses += guess + " "

        if turns == 0:
            print(colored("You Loose!", "red")) # color text. wait fot test in cmd

    print(f"Wrong letters are: {wrong_guesses}")
    print(man[MAX_TURNS - turns])
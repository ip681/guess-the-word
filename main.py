import random
from termcolor import colored

current_theme = ""
theme_name = ""
words = ""
guesses = ""
wrong_guesses = ""
MAX_TURNS = 12
turns = 12

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

theme_animals = ['cat', 'dog', 'monkey', 'cow', 'crocodile', 'elephant', 'lion', 'tiger', 'giraffe', 'zebra']
theme_birds = ['raven', 'eagle', 'duck', 'sparrow', 'pigeon', 'parrot', 'seagull', 'pelican', 'flamingo', 'marabou']
theme_jobs = ['programmer', 'analyst', 'actor', 'singer', 'engineer', 'architect', 'barber', 'scientist', 'lawyer', 'designer']
theme_body_parts = ['head', 'neck', 'arm', 'foot', 'leg', 'hand', 'chest', 'knee', 'elbow', 'ankle']

theme_index = random.choice(range(0, 4))

if theme_index == 0:
    theme_name = "animals"
    words = theme_animals
elif theme_index == 1:
    theme_name = "birds"
    words = theme_birds
elif theme_index == 2:
    theme_name = "jobs"
    words = theme_jobs
elif theme_index == 3:
    theme_name = "parts of body"
    words = theme_body_parts

word = random.choice(words)

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

print(f"Guess the word! Theme is {theme_name.upper()}")
while turns > 0:

    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print("")  # new line

    if failed == 0:
        print(colored("You Win!", "green"))
        print(f"The word is: {word.upper()}")
        break

    print()

    while True:
        print("____________________________________________________________________\n")

        guess = input("Input letter: ")

        if guesses.find(str(guess)) != -1: # if repeat wrong guess don't lose try and output message
            print(f"You already try the letter {guess}")
            turns += 1

        if len(guess) == 1 and guess.isalpha():  # check for more than one character and not letter character
            guess = guess.lower()  # make the letter lowercase if it is uppercase
            break
        else:
            print("Enter a single letter (a-z).")
            continue

    guesses += guess

    if guess not in word:  # checks if the letter entered is part of a word
        turns -= 1
        print(f"Wrong! You have {turns} more guesses")
        wrong_guesses += guess + " "

        if turns == 0:
            print(colored("You Loose!", "red"))  # color text. wait fot test in cmd
            print(f"The word is: {word.upper()}")

    print(f'Theme is {theme_name.upper()}')
    print(f"Wrong letters are: {wrong_guesses}")
    print(man[MAX_TURNS - turns])
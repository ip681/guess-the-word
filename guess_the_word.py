import random

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
print("Guess the word")
guesses = ""
wrong_letters = ""
turns = 12
while turns > 0:
    print("___________________________________________________________________")
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print("")
    if failed == 0:
        print("You Win!")
        print(f"The word is: {word}")
        break
    print()
    while True:
        guess = input('Input letter: ')

        if len(guess) == 1 and guess.isalpha():
            print(guess.lower())
            break

        else:
            print('Enter a single letter (a-z).')
            continue
    guesses += guess
    if guess not in word:
        turns -= 1
        print(f"Wrong! You have {turns} more guesses")
        wrong_letters += guess + " "
        if turns == 0:
            print("You Loose!")
    print(f"Wrong letters are: {wrong_letters}")
    print(man[12 - turns])
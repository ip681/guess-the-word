import random
words = ['cat', 'computer', 'coffee']
word = random.choice(words)
print("Guess the word")
guesses = ""
wrong_letters = ""
turns = 12
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print("")
    print("___________________________________________________________________")
    if failed == 0:
        print("You Win!")
        print("The word is: ", word)
        break
    print()
    guess = input("Input letter:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong! You have", + turns, 'more guesses')
        wrong_letters += guess + " "
        if turns == 0:
            print("You Loose!")
    print(f"Wrong letters are: {wrong_letters}")
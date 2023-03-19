# 6. Write a Python program to guess a number between 1 and 9.
# User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

num = 7
while True:
    guess = int(input("Guess a number between 1-9 : "))
    if guess == num:
        print("Well guessed!")
        break

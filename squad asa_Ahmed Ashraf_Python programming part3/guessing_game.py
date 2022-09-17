secret_word = "Hello"
number_of_guesses = 3
guesses_left = True
guess = ""

while guess != secret_word and guesses_left :
    guess = input("Number of guesses left = " + str(number_of_guesses) + " Enter your guess: ")
    if guess == secret_word:
        print("Congrats you won!!")
        quit()
    else:
        number_of_guesses -= 1

    if number_of_guesses == 0:
        print("You lost!!")
        quit()
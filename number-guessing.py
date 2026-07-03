# NUMBER GUESSING GAME
# ====================

import random

# While the player wants to play:
while True:

    # generate a rand num
    secret = random.randint(1, 10)

    # reset the attempt counter
    attempt = 0

    # ask for guesses until the guess is correct
    print("GUESS A NUMBER (1-10)")
    user_guess = int(input("Guess: "))

    while user_guess != secret:

        # count every guess
        attempt += 1

        # input validation
        if user_guess < 1 or user_guess > 10:
            print("Please enter a number between 1 and 10.")

        elif user_guess < secret:
            print("Too Low")

        elif user_guess > secret:
            print("Too High")

        # ask again
        user_guess = int(input("Guess: "))

    # count the final correct guess
    attempt += 1

    print("Correct!")

    # tell the player how many attempts it took
    print("===============================")
    print(f"This took {attempt} attempts.")
    
    # ask if they want to play again
    play_again = input("Play Again? (yes or no): ")
    print("===============================")

    if play_again == "no":
        print("Thanks for Playing!")
        break

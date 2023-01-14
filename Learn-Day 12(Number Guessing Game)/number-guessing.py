import random
import art

RANDOM_SCORE = random.randint(1, 100)

difficulty = {
    "hard": 5,
    "easy": 10
}
print(type(RANDOM_SCORE))
print(RANDOM_SCORE)


def compare(guess, turns):
    if guess > RANDOM_SCORE:
        print("Too high.")
        return turns - 1
    elif guess < RANDOM_SCORE:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {RANDOM_SCORE}.")


def play():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of the number between 1 and 100")
    difficulty_choice = input("Choose the difficulty. Type 'easy' or 'hard': ")

    lives = difficulty[difficulty_choice]
    user_guess = 0
    while user_guess != RANDOM_SCORE:
        print(f"You have {lives} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        lives = compare(user_guess, lives)
        if lives == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != RANDOM_SCORE:
            print("Guess again.")


play()

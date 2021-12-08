# youtuber = "James"

# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Your guess is too low. TRY AGAIN")
        elif guess > random_number:
            print("Your guess is too high. TRY AGAIN")
        else:
            print("You got it! Luck bastard")

guess(10)





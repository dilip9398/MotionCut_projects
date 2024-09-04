import random
guess = random.randint(1,99)
num = int(input("Enter the number: "))


while guess != num:
    if guess < num:
        print("Your guess is too low.")
    elif guess > num :
        print("Your guess is too high.")
    guess = int(input("Guess again: "))
print("Your guess is correct.")

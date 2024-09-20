import random
print("Welcome to the number guessing game!\n You have got 5 chances \n Guess the Number now")
print("""
           ________
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####
                       d###P
                    _g###@F
                 _gN##@P
               gN###F"
              d###F
             0###F
             0###F
             0###F
             "NN@'

              ___
             q###r
             """)
def play_game():
    number_guess = random.randrange(100)

    chances = 5
    counter_guess = 0

    while counter_guess <= chances:

        counter_guess += 1
        guess = input("Guess the Number: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Enter the valid number!")
            continue

        if guess == number_guess:
            print("You Guessed the correct number!\n Your IQ levels are Good!")
            break
        elif counter_guess == chances and guess != number_guess:
            print(f"Sorry! Better luck next time!. The Number is {number_guess}")
        elif guess < number_guess:
            print("Your guess is lower!")
        elif guess > number_guess:
            print("Your guess is Higher!")
            
            
    play_again = input("Do you want to guess again? (Y/N)")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thankyou for playing!")

play_game()

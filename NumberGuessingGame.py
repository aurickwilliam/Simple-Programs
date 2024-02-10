import random

print("Welcome to the Number Guessing Game!\n\n")

print("I've Selected a number between 1 and 100.\nTry to guess it!\n") 

target_number = random.randrange(1, 101) 
number_of_guesses = 0 
user_guess = 0

isPlaying = True 
while isPlaying:
    user_guess = int(input("Enter your guess: "))

    if user_guess == target_number:
        number_of_guesses += 1
        print("Congratulations! You guessed the number + str(target_number) + " in
              " + str(number_of_guesses) + guesses\n\n")
        
        isPlayAgain = True
        while isPlayAgain:
            play_again = input("Do you want to play again (Y/N)? ")
            if play_again.upper() == "Y":
                print("\n\n\nI've Selected a number between 1 and 100.\nTry to guess it!\n") 
                target_number = random.randrange(1, 101)
                break
            elif play_again.upper() == "N":
                isPlaying = False
                break
            else:
                print("Please enter the valid input!") 
                continue

    elif user_guess > target_number:
        number_of_guesses += 1
        print("Too High! Try again") 
    elif user_guess < target_number: 
        number_of_guesses += 1
        print("Too Low! Try Again")
    else:
        print("Please enter a valid input!")

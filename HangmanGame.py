import random

print(" #     #    #    #     #  #####     #     #    #    #     # ")
print(" #     #   # #   ##    # #     #    ##   ##   # #   ##    # ")
print(" #     #  #   #  # #   # #          # # # #  #   #  # #   # ")
print(" ####### #     # #  #  # #  ####    #  #  # #     # #  #  # ")
print(" #     # ####### #   # # #     #    #     # ####### #   # # ")
print(" #     # #     # #    ## #     #    #     # #     # #    ## ")
print(" #     # #     # #     #  #####     #     # #     # #     # ")

print("\n\nA random word will be selected, try and guess each letter of it.")
print("\nGuess the word before the stickman hangs to death!\n\n")

categories = ("Food", "Countries", "Car")

categ_Food = ("Broccoli",
              "Brownie",
              "Cabbage",
              "Doughnut",
              "Macaroni",
              "Lasagna",
              "Mushroom",
              "Sausages",
              "Spaghetti",
              "Watermelon")

categ_Country = ("South Korea",
                 "China",
                 "Afghanistan",
                 "America",
                 "Palestine",
                 "Japan",
                 "Indonesia",
                 "Singapore",
                 "Russia",
                 "United Kingdom",
                 "Spain")

categ_Car = ("Toyota",
             "Aston Martin",
             "Mitsubishi",
             "Suzuki",
             "Volkswagen",
             "Lamborghini",
             "Bugatti",
             "Peugeot",
             "Tesla",
             "Ford",
             "Mercedes")
Hangman9 = ["           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "=========="]
Hangman8 = ["           ",
            "         | ",
            "         | ",
            "         | ",
            "         | ",
            "         | ",
            "=========="]
Hangman7 = ["   +-----+ ",
            "         | ",
            "         | ",
            "         | ",
            "         | ",
            "         | ",
            "=========="]
Hangman6 = ["   +-----+ ",
            "         | ",
            "   O     | ",
            "         | ",
            "         | ",
            "         | ",
            "=========="]
Hangman5 = ["   +-----+ ",
            "         | ",
            "   O     | ",
            "  /      | ",
            "         | ",
            "         | ",
            "=========="]
Hangman4 = ["   +-----+ ",
            "         | ",
            "   O     | ",
            "  /|     | ",
            "         | ",
            "         | ",
            "=========="]
Hangman3 = ["   +-----+ ",
            "         | ",
            "   O     | ",
            "  /|\\    | ",
            "         | ",
            "         | ",
            "=========="]
Hangman2 = ["   +-----+ ",
            "         | ",
            "   O     | ",
            "  /|\\    | ",
            "  /      | ",
            "         | ",
            "=========="]
Hangman1 = ["   +-----+ ",
            "         | ",
            "   O     | ",
            "  /|\\    | ",
            "  / \\    | ",
            "         | ",
            "=========="]
Hangman0 = ["   +-----+ ",
            "   |     | ",
            "   0     | ",
            "  /|\\    | ",
            "  / \\    | ",
            "         | ",
            "=========="]

Chosen_Word = ""
Index = 0
Lives = 10
list_of_Guess = ""


def Generate_Word(categ):
    if categ == 'A':
        Index = random.randrange(0, len(categ_Food))
        word = categ_Food[Index]
        catergory = "Food"
    elif categ == 'B':
        Index = random.randrange(0, len(categ_Country))
        word = categ_Country[Index]
        catergory = "Countries"
    elif categ == 'C':
        Index = random.randrange(0, len(categ_Car))
        word = categ_Car[Index]
        catergory = "Cars"
    else:
        return "Error"

    return word


def Generate_Underlines(word, letter):
    preview_word = ""

    for i in word:
        for j in letter:
            if i == j:
                preview_word += j + " "
                break
            elif j == letter[-1]:
                preview_word += "_ "

    return preview_word


def print_hangman(Lives):
    hangman = ""
    display = None

    if Lives == 9:
        display = Hangman9
    elif Lives == 8:
        display = Hangman8
    elif Lives == 7:
        display = Hangman7
    elif Lives == 6:
        display = Hangman6
    elif Lives == 5:
        display = Hangman5
    elif Lives == 4:
        display = Hangman5
    elif Lives == 3:
        display = Hangman3
    elif Lives == 2:
        display = Hangman2
    elif Lives == 1:
        display = Hangman1
    elif Lives == 0:
        display = Hangman0
    else:
        display = "\n\n\n"

    for i in display:
        hangman += i + "\n"

    return hangman


isPlaying = True
while isPlaying:
    Lives = 10
    list_of_Guess = ""

    print("==============================")
    print("Categories:")
    print("A -> Food")
    print("B -> Countries")
    print("C -> Cars")
    print("==============================\n")

    while True:
        Chosen_Categ = input("Enter the Category: ")

        if Generate_Word(Chosen_Categ.upper()) == "Error":
            print("\nInvalid Input\n")
            continue
        else:
            Chosen_Word = Generate_Word(Chosen_Categ.upper())
            break

    # print(Chosen_Word)
    print("Game Start!\n\n")

    print(Generate_Underlines(Chosen_Word, " "))

    while Lives > 0:

        while True:
            user_guess = input("\nEnter your guess letter: ").lower()

            if len(user_guess) > 1:
                print("\nInvalid Input!")
                continue
            elif not user_guess.isalpha():
                print("\nInvalid Input!")
                continue
            elif user_guess in list_of_Guess:
                print("You already guess this letter!")
                continue
            else:
                list_of_Guess = list_of_Guess + user_guess
                break
        verify_guess = Generate_Underlines(Chosen_Word.lower(), list_of_Guess)

        if user_guess not in Chosen_Word.lower():
            Lives -= 1

        print()
        print(print_hangman(Lives))
        print("\n\n" + verify_guess)

        if "_ " not in verify_guess:
            print("\n\nHooray!! You Have guess the word!")
            print("The word is: " + Chosen_Word)
            break

    if Lives == 0:
        print("The man is dead! :(\nGame Over!\n\n")

    while True:
        play_again = input("\nDo you want to play again? (Y/N)")
        if play_again.lower() == 'y':
            break
        elif play_again.lower() == 'n':
            print("Thank you for Playing!\n\n")
            isPlaying = False
            break
        else:
            print("\nInvalid Input!\n")

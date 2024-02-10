import random

print("Let's Play Rock, Paper, Scissor Game!!")

hands = ["rock", "paper", "scissor"]
def process(player, computer):
    result = ""
    if player.lower() == "rock":
        if computer == "rock":
            result = "Draw"
        elif computer == "scissor":
            result = "Winner"
        else:
            result = "Loser"
    elif player.lower() == "paper":
        if computer == "paper":
            result = "Draw"
        elif computer == "rock":
            result = "Winner"
        else:
            result = "Loser"
    elif player.lower() == "scissor":
        if computer == "scissor":
            result = "Draw"
        elif computer == "paper":
            result = "Winner"
        else:
            result = "Loser"
    return result

isPlaying = True
while isPlaying:
    player_hand = input("\nEnter your pick (Rock, Paper, Scissor): ")
    number = random.randrange(0, 3)
    computer_hand = hands[number]
    if player_hand.lower() not in hands:
        print("Please enter the correct value!")
        continue
    print("Computer: " + computer_hand)
    print("\nResult of the Game: " + process(player_hand, computer_hand))
    
    isTryAgain = True
    while isTryAgain:
        again = input("\n\nTry Again (Y/N): ")
        if again.lower() == "y":
            isTryAgain = False
        elif again.lower() == "n":
            print("Thank you for Playing!")
            isPlaying = False
            break
        else:
            print("Invalid Input! Please Try Again!")\
            
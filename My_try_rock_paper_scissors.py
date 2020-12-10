from random import randint

choices = ["R", "P", "S"]
computer_choice = choices[randint(0,2)]

# Player did not play yet
player = False

while player is False:
    player = input("Choose Rock, Paper or Scissors: ")
    if player not in choices:
        print("Invalid Input")
    elif player == computer_choice:
        print("It is a tie")
    elif player == choices[0] and computer_choice == "P":
        print(f"You Lose, {computer_choice} covers {player}")
    elif player == choices[0] and computer_choice == "S":
        print(f"You Win, {player} smashes {computer_choice}")
    elif player == choices[1] and computer_choice == "R":
        print(f"You Win, {player} covers {computer_choice}")
    elif player == choices[1] and computer_choice == "S":
        print(f"You Lose, {computer_choice} cut {player}")
    elif player == choices[2] and computer_choice == "R":
        print(f"You Lose, {computer_choice} smashes {player}")
    elif player == choices[2] and computer_choice == "P":
        print(f"You Win, {player} cut {computer_choice}")

    player = False
    computer_choice = choices[randint(0, 2)]
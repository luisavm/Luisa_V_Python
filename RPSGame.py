from random import randint

computer_lives = 5
player_lives = 5

# available weapones => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# computer randomly select option
computer = choices[randint(0, 2)]


# define a win or lose with a more efficient way
def winorlose(status):
    # handle win or lose based on the status we pass in
    print("****************")
    print("You", status, "!", "Would you like to play again?")
    choice = input("Y / N?")

    if choice == "Y" or choice == "y":
        # we reset the player lives
        # change global variable
        global player_lives
        global computer_lives
        global player
        global computer

        player_lives = 5
        computer_lives = 5
        player = False
        computer = choices[randint(0, 2)]

    if choice == "N" or choice == "n":
        print("You quit! Bye bye!")
        print("*******************")
        exit()


# show the computer's choice in the terminal window
# print("computer chooses: ", computer)

while player is False:
    print("=======================================")
    print("Player Lives:", player_lives, "/5")
    print("AI Lives:", computer_lives, "/5")
    print("=======================================")
    print("Choose your weapon!\n")
    player = input("Rock, Paper, or Scissors?\n")
    print("player choose:", player)

    # Tie: no one wins NAHHHH
    if (player == computer):
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            # if computer chooses paper, player plays rock
            # the computer will win, player will lose
            player_lives -= 1
            print("You lose", computer, "covers", player, "\n")
        else:
            # player wins, computer will lose
            computer_lives -= 1
            print("You win!", player, "smashes", computer)

    elif player == "Paper":
        if computer == "Scissors":
            # if computer responds with scissors, player chooses paper
            # the computer will win, player will lose
            player_lives -= 1
            print("You lose", computer, "cuts", player)
        else:
            # player wins, computer will lose
            computer_lives -= 1
            print("You win!", player, "covers", computer)

    elif player == "Scissors":
        if computer == "Rock":
            # if computer chooses rock, player responds with scissors
            # the computer will win, player will lose
            player_lives -= 1
            print("You lose", computer, "smashes", player)
        else:
            # player wins, computer will lose
            computer_lives -= 1
            print("You win!", player, "cuts", computer)

    elif player == "Quit" or player == "quit":
        exit()

    else:
        print("Not a valid option. Check again, and check your spelling!\n")

    # handle win or lose
    if player_lives is 0:
        winorlose("lost")

    elif computer_lives is 0:
        winorlose("won")

    player = False
    computer = choices[randint(0, 2)]

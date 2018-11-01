from random import randint

# available weapones => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

computer_lives = 3
player_lives = 3

# computer randomly select option
computer = choices[randint(0, 2)]

# player randomly select option for weapones
player = choices[randint(0, 2)]

# Tie: no one wins NAHHHH
if (player == computer):
        print("Tie! Live to shoot another day")

elif player == "Rock":
        if computer == "Paper":
            # if computer chooses paper, player plays rock
            # the computer will win, player will lose
            player_lives == player_lives
            print("You lose", computer, "covers", player)
        else:
            # player wins, computer will lose
            computer_lives == computer_lives
            print("You win!", player, "smashes", computer)

elif player == "Paper":
        if computer == "Scissors":
            # if computer responds with scissors, player chooses paper
            # the computer will win, player will lose
            player_lives == player_lives
            print("You lose", computer, "cuts", player)
        else:
            # player wins, computer will lose
            computer_lives == computer_lives
            print("You win!", player, "covers", computer)

elif player == "Scissors":
        if computer == "Rock":
            # if computer chooses rock, player responds with scissors
            # the computer will win, player will lose
            player_lives == player_lives
            print("You lose", computer, "smashes", player)
        else:
            # player wins, computer will lose
            computer_lives == computer_lives
            print("You win!", player, "cuts", computer)

elif player == "Quit":
        exit()

else:
        print("Not a valid option. Check again, and check your spelling!\n")

        player = False
        computer = choices[randint(0, 2)]

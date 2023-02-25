# 3. Rock-paper-scissors
# The objective of this task is to create a program that plays the rock-paper-scissors game with the user.
#
# Write a function called play, which has two parameters: choices of both players as strings ("rock", "paper", or "scissors"). The
# function should return "first" if the first player wins and "second" if the second player wins. If the values given to the function are
# the same, then it should return "draw".
#
# Write a program that first asks the user for a number of turns. Then it asks the user to choose either rock, paper, or scissors. It can
# be assumed that the inputs are correct. The program generates its random choice and outputs the result using the function play. At each
# turn, the program also outputs the current score, i.e., the number of wins of both players.
#
# This is repeated the specified number of turns. At the end of the game, the program outputs the final result: whether the user won,
# lost or the game ended in a draw.
#
# Example
#
# Enter number of turns: 3
# Enter your choice: scissors
# Computer chose scissors. Draw! You 0, computer 0.
# Enter your choice: rock
# Computer chose scissors. You win! You 1, computer 0.
# Enter your choice: rock
# Computer chose paper. Computer wins! You 1, computer 1.
# The game ended in a draw.
#
# Hint. To make random choices, you generate a random number from 1 to 3 and choose the value "rock", "paper", or "scissors" accordingly.
#
# >>> from random import randint
# >>> randint(1, 3)
# 3
# >>> randint(1, 3)
# 1

from random import randint

def play(player1, player2):
    if player1 == player2:
        return "draw"
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        return "first"
    else:
        return "second"

print("Enter number of turns:")
turns = int(input())

score1 = 0
score2 = 0

for turn in range(turns):
    print("Enter your choice:")
    player1 = input()
    player2 = ""
    if randint(1, 3) == 1:
        player2 = "rock"
    elif randint(1, 3) == 2:
        player2 = "paper"
    else:
        player2 = "scissors"
    print("Computer chose " + player2 + ".")
    result = play(player1, player2)
    if result == "first":
        score1 += 1
        print("You win! You " + str(score1) + ", computer " + str(score2) + ".")
    elif result == "second":
        score2 += 1
        print("Computer wins! You " + str(score1) + ", computer " + str(score2) + ".")
    else:
        print("Draw! You " + str(score1) + ", computer " + str(score2) + ".")

if score1 > score2:
    print("You won!")
elif score1 < score2:
    print("You lost!")
else:
    print("The game ended in a draw.")

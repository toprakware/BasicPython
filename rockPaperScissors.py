#Toprk

from random import randint

print("""\nROCK-PAPER-SCISSORS SIMULATOR (STILL WORKS 2020)\n""")

computer_point,player_point = 0,0
draw_count = 0

while True:

    num = randint(0,2)
    computer = ""

    if num == 0:
        computer = "ROCK"
    elif num == 1:
        computer = "PAPER"
    elif num == 2:
        computer = "SCISSORS"

    print("Press (Q) to Quit")
    player = input("\n  TYPE HERE: ")
    player = player.upper()

    if player not in ("ROCK","PAPER","SCISSORS","Q"):
        print("Invalid Input\n")
        continue

    if player == "Q":
        break
    elif player == "ROCK" and computer == "ROCK":
        print("****************")
        print("  DRAW!")
        print("****************")
        draw_count += 1
    elif player == "PAPER" and computer == "PAPER":
        print("****************")
        print("  DRAW!")
        print("****************")
        draw_count += 1
    elif player == "SCISSORS" and computer == "SCISSORS":
        print("****************")
        print("  DRAW!")
        print("****************")
        draw_count += 1


    if computer == "ROCK" and player == "PAPER":
        print("****************")
        print("  PLAYER WINS!")
        print("****************")
        player_point += 1
    elif computer == "ROCK" and player == "SCISSORS":
        print("****************")
        print("  COMPUTER WINS!")
        print("****************")
        computer_point += 1
    elif computer == "PAPER" and player == "SCISSORS":
        print("****************")
        print("  PLAYER WINS!")
        print("****************")
        player_point += 1


    if player == "ROCK" and computer == "PAPER":
        print("****************")
        print("  COMPUTER WINS!")
        print("****************")
        computer_point += 1
    elif player == "ROCK" and computer == "SCISSORS":
        print("****************")
        print("  PLAYER WINS!")
        print("****************")
        player_point += 1
    elif player == "PAPER" and computer == "SCISSORS":
        print("****************")
        print("  COMPUTER WINS!")
        print("****************")
        computer_point += 1

print(f"""
*********************************
PLAYER WON: {player_point} times
---------------------------------
COMPUTER WON: {computer_point} times
---------------------------------
DRAW: {draw_count}
*********************************
""")

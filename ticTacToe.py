#Toprk

print("\nTIC-TAC-TOE LEGIT FUN (Proven working 2021)")

L = ["-","-","-","-","-","-","-","-","-"]

print(f"""
    -------------------------
    1   {L[0]}   * 2  {L[1]}   * 3  {L[2]}         
    -------------------------
    4   {L[3]}   * 5  {L[4]}   * 6  {L[5]}
    -------------------------
    7   {L[6]}   * 8  {L[7]}   * 9  {L[8]}
    -------------------------
    """)

played_list = []
isPlayer1sTurn = True
isPlayer1Won   = False
isPlayer2Won   = False

while True:

    if isPlayer1sTurn:
        try:
            place = int(input("Place to which Tile? (Player1) (X): "))
            
            if place in played_list:
                print("This tile is taken.")
                continue
            elif place <= 0 or place >= 10:
                print("Invalid Input. Use numbers between 1-9s")

            played_list.append(place)
        except ValueError:
            print("Invalid Input. Use numbers between 1-9")
            continue

        isPlayer1sTurn = False
        L[place - 1] = "X"
    else:
        try:
            place = int(input(f"Place to which Tile? (Player2) (O): "))

            if place in played_list:
                print("This tile is taken.")
                continue
            elif place <= 0 or place >= 10:
                print("Invalid Input. Use numbers between 1-9s")

            played_list.append(place)
        except ValueError:
            print("Invalid Input. Use numbers between 1-9")
            continue

        isPlayer1sTurn = True
        L[place - 1] = "O"


    print(f"""
    -------------------------
    1   {L[0]}   * 2  {L[1]}   * 3  {L[2]}         
    -------------------------
    4   {L[3]}   * 5  {L[4]}   * 6  {L[5]}
    -------------------------
    7   {L[6]}   * 8  {L[7]}   * 9  {L[8]}
    -------------------------
    """)


    if L[0] == "X" and L[1] == "X" and L[2] == "X":
        isPlayer1Won = True
    elif L[0] == "O" and L[1] == "O" and L[2] == "O":
        isPlayer2Won = True

    if L[3] == "X" and L[4] == "X" and L[5] == "X":
        isPlayer1Won = True
    elif L[3] == "O" and L[4] == "O" and L[5] == "O":
        isPlayer2Won = True

    if L[6] == "X" and L[7] == "X" and L[8] == "X":
        isPlayer1Won = True
    elif L[6] == "O" and L[7] == "O" and L[8] == "O":
        isPlayer2Won = True

    if L[0] == "X" and L[3] == "X" and L[6] == "X":
        isPlayer1Won = True
    elif L[0] == "O" and L[3] == "O" and L[6] == "O":
        isPlayer2Won = True

    if L[1] == "X" and L[4] == "X" and L[7] == "X":
        isPlayer1Won = True
    elif L[1] == "O" and L[4] == "O" and L[7] == "O":
        isPlayer2Won = True

    if L[2] == "X" and L[5] == "X" and L[8] == "X":
        isPlayer1Won = True
    elif L[2] == "O" and L[5] == "O" and L[8] == "O":
        isPlayer2Won = True

    if L[0] == "X" and L[4] == "X" and L[8] == "X":
        isPlayer1Won = True
    elif L[0] == "O" and L[4] == "O" and L[8] == "O":
        isPlayer2Won = True

    if L[2] == "X" and L[4] == "X" and L[6] == "X":
        isPlayer1Won = True
    elif L[2] == "O" and L[4] == "O" and L[6] == "O":
        isPlayer2Won = True


    if isPlayer1Won:
        print("Player1 WINS!")
        break
    elif isPlayer2Won:
        print("Player2 WINS!")
        break

    if "-" not in L:
        print("Game Ended. Draw!")
        break


print(f"""
    -------------------------
    1   {L[0]}   * 2  {L[1]}   * 3  {L[2]}         
    -------------------------
    4   {L[3]}   * 5  {L[4]}   * 6  {L[5]}
    -------------------------
    7   {L[6]}   * 8  {L[7]}   * 9  {L[8]}
    -------------------------
    """)

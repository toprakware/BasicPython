#@toprakware

from random import randint

print("** Hello, Let's play a number guessing game! **")
print(" --  Guess a number between 0-10 --  ")
print("\nTry to find the secret number!")

selected_number = randint(0, 10)                             #The selected number by computer.
lives           = 3                                          #Lives left.
tries           = 0                                          #Tries start with 0. (No way)
guessed_list    = []                                         #The list that will remember what's
                                                             #guessed before.
while True:
    try:
        guess = int(input("Your Guess: "))                   #Checks whether the input (guess)
    except ValueError:                                       #is an integer or not.
        print("Please type an (+) integer. (Between 0-10)")
        continue
    
    if guess in guessed_list:                                #Checks if it has been used before.
        print("You already guessed this number.")
        print("********************")                        #Cool decorations.
        continue
    guessed_list.append(guess)                               #Saves the guesses.

    tries += 1                                               #Adds +1 to the tries variable per input.            

    if int(guess) < 0 or int(guess) > 10:                    #Checks whether the input (guess)
        print("Please type a number between 0 and 10.")      #in the given value range or not.
        continue

    if guess == selected_number and tries == 1:              #If found within first try.
        print("BULLSEYE! You found it first try.")
        break

    elif guess == selected_number:                           #If guessed right.
        print("\nNice! You found it after", tries, "tries.")
        break
    else:                                                    #If guessed wrong.
        lives -= 1
        print("Try Again. :( Lives left: ", lives)

    if lives <= 0:                                           #If no more lives are left.
        print("\nYou don't have any lives left. The selected number by computer was", selected_number)
        break

    print("********************")                            #Cool decorations

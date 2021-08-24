#Toprk

from random import choice

print("""
    ***** PLAY HANGMAN WITH ME *****
    Hello, let's play hangman!
    """)

word_list    = []
harder_list  = ["unhappiness", "pessimism", "spitefulness", "javascript"]
easier_list  = ["linux", "macbook", "python", "swift", "chaos", "bad life"]
guess_list   = []      #Guessed words get added to this list.

lives        = 10      #Lives left.
tries        = 0
guess_string = ""      #Guessed words get added to this string.

while True:
    difficulty = input("Select Difficulty (EASY/HARD): ")            #Selecting difficulty.
    if difficulty in ("EASY","easy","Easy"):
        word_list = easier_list
        break
    elif difficulty in ("HARD","hard","Hard"):
        word_list = harder_list
        break
    else:
        print("Please select a valid difficulty level EASY or HARD")
        continue

secret_word  = choice(word_list)   #A random word from the word_list gets selected as the secret word

while True:
    character_left = 0 
    #Resets remaining character count after every time the while loop repeats.
    #If it doesn't get reset it continues while getting added into it. (This isn't a good thing)

    for character in secret_word:
        if character in guess_string:
            print(character, end=" ")
        else:
            #If there is a character that's not found, if fills that characters spot with a "-".                
            print("-", end=" ")  
            character_left += 1
            #Remaining character count won't reach 0 until all the characters are found.

    #If the remaining character count reaches zero:
    if character_left <= 0:
        #The game ends!
        print("\nWOW! You won after", tries, "tries!")
        break
    
    guess = input("\nYour Guess: ")
    tries += 1                        #Adds +1 to the tries variable per input.
    guess_string += guess

    try:
        #If the input (guess) can be converted into an integer,
        #it means that the input was entered as an integer.
        int(guess)
        print("Please type a letter.")
        continue
    except ValueError:
        pass

    print("************************")   #Cool decorations.

    #If the entered letter count is more than one, it gives out an error.
    #Unless the secret word gets entered
    if len(guess) > 1 and guess != secret_word:  
        print("Try again with only using 1 letter or type better guess next time.")
        break

    #If this letter (guess) was guessed before.
    if guess in guess_list:
        print("You already guessed this letter, try again.")

    elif guess in secret_word:
        print("Nice One!")

    elif guess not in secret_word:

        if lives <= 0:
            print("You don't have any lives left. The secret word was", secret_word)
            break

        lives -= 1
        print("TRY AGAIN!, You have", lives, "lives left.")

    print("************************")         #Cool decorations again.
    
    guess_list.append(guess)                  #Saves the past guesses to a list.

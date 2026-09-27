import random
while True:

    attempt = 0
                        
    print("1. Easy mode: [1,30] with 10 attempts")
    print("2. Normal mode: [1,70] with 7 attempts")
    print("3. Hard mode: [1,100] with 5 attempts")
    print("4. God mode: [1,250] with 3 attempts")
    
    # difficulty loop
    while True:
        try:

            difficulty = int(input("Select your game mode (1-4): "))
            if 1 <= difficulty <= 4:
              break
            print("Dumboo, you can't even pick a valid number between 1 and 4!")
        except ValueError:
            print("Bruh really just put the right numbers")
        continue 

    if difficulty == 1:
        max_range = 30
        max_attempts = 10
    elif difficulty == 2:
        max_range = 70
        max_attempts = 7
    elif difficulty == 3:
        max_range = 100
        max_attempts = 5
    elif difficulty == 4:
        max_range = 250
        max_attempts = 3

    number = random.randint(1, max_range)

    #guess loop
    while True:
        try:
            guess = int(input(
                f"Input the desired number (between 1 and {max_range}): "))
        except ValueError:
            print("Please enter a number!")
            continue

        if guess > max_range or guess < 1:
            print("Dumboo can't you read?")
            continue
        

        attempt += 1

        if guess == number:
            print(f"Well done homie you got it in {attempt} attempts.")
            break                 
        
        elif guess > number:
            print(f"Your guess is higher and attempt count is {attempt}, remaining attempts are {max_attempts - attempt}")
        else:
            print(f"Your guess is lower and attempt count is {attempt}, remaining attempts are {max_attempts - attempt}")
        
        if attempt == (max_attempts):
            print("You lost the game better luck next time, try again.")
            print(f"The number was {number}")
            break

    ans = input("If you want to play again type [Y/N]:")
    if ans == "Y":
        continue
    else:
        break

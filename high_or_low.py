def high_low(guess, number, attempt):
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
           print("Too high.")
        elif guess < number:
           print("Too low.")
        else:
            print(f"You got it! The answer was {number}.")
            break
        attempt -= 1
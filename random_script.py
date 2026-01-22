import random

# Simple random number guessing game
def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("🎮 Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100...\n")
    
    while not guessed:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("📈 Too low! Try again.")
            elif guess > secret_number:
                print("📉 Too high! Try again.")
            else:
                print(f"\n🎉 You got it! The number was {secret_number}!")
                print(f"It took you {attempts} attempts!")
                guessed = True
        except ValueError:
            print("⚠️  Please enter a valid number!")

if __name__ == "__main__":
    guess_the_number()

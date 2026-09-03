import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("=" * 45)
    print("🎮 NUMBER GUESSING SHOWDOWN (1 to 100) 🎮")
    print(f"You have {max_attempts} attempts to crack the code!")
    print("=" * 45)

    while attempts < max_attempts:
        try:
            guess = int(input(f"\n[Attempt {attempts + 1}/{max_attempts}] Enter your guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter an integer.")
            continue

        attempts += 1

        if guess == number_to_guess:
            score = (max_attempts - attempts + 1) * 10
            print(f"\n🎉 BOOM! You got it in {attempts} tries!")
            print(f"⭐ Your Score: {score}/70")
            break
        elif guess < number_to_guess:
            print("🔻 Too low! Think bigger.")
        else:
            print("🔺 Too high! Go lower.")
    else:
        print(f"\n💀 Game Over! The hidden number was {number_to_guess}.")

if __name__ == "__main__":
    play_game()
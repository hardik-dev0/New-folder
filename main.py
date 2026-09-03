import random

def get_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")
    
    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == "1":
            return 10
        elif choice == "2":
            return 7
        elif choice == "3":
            return 5
        print("❌ Invalid selection! Type 1, 2, or 3.")

def play_round():
    max_attempts = get_difficulty()
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("\n" + "=" * 45)
    print("🎮 NUMBER GUESSING SHOWDOWN (1 to 100) 🎮")
    print(f"You have {max_attempts} attempts to crack the code!")
    print("=" * 45)

    while attempts < max_attempts:
        try:
            guess = int(input(f"\n[Attempt {attempts + 1}/{max_attempts}] Enter guess: "))
        except ValueError:
            print("❌ Invalid input! Numbers only.")
            continue

        attempts += 1

        if guess == number_to_guess:
            score = (max_attempts - attempts + 1) * 10
            print(f"\n🎉 BOOM! You got it in {attempts} tries!")
            print(f"⭐ Score: {score}")
            return
        elif guess < number_to_guess:
            print("🔻 Too low! Aim higher.")
        else:
            print("🔺 Too high! Aim lower.")

    print(f"\n💀 Out of tries! The correct number was {number_to_guess}.")

def main():
    while True:
        play_round()
        replay = input("\nPlay another round? (y/n): ").strip().lower()
        if replay != 'y':
            print("\nThanks for playing! Catch you later. 🚀")
            break

if __name__ == "__main__":
    main()
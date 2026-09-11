import random

print("\n" + "=" * 50)
print("          🎯 GUESS THE NUMBER GAME")
print("=" * 50)
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it!\n")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess == secret_number:
            print("\n🎉 Correct!")
            print(f"You guessed the number in {attempts} attempts.")
            print(f"The number was {secret_number}.")
            break

        elif user_guess > secret_number:
            print("📉 Too high! Try a lower number.\n")

        else:
            print("📈 Too low! Try a higher number.\n")

    except ValueError:
        print("⚠️ Please enter a valid number.\n")

print("\nThanks for playing! 👋")
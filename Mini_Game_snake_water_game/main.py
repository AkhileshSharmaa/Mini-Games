import random

def play_game():
    """Play Snake, Water, Gun and keep track of the score."""

    print("\n------------ Welcome to Snake, Water, Gun Game ------------")
    print('Press "1" for Snake 🐍')
    print('Press "2" for Water 💧')
    print('Press "3" for Gun 🔫')

    user_score = 0
    computer_score = 0
    draws = 0

    while True:
        try:
            user_choice = int(input("\nPick a number (1-3): "))
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 3.")
            continue

        if user_choice not in [1, 2, 3]:
            print("❌ Invalid choice! Please choose 1, 2, or 3.")
            continue

        computer_choice = random.choice([1, 2, 3])

        game_elements = {
            1: "Snake 🐍",
            2: "Water 💧",
            3: "Gun 🔫"
        }

        print(f'\nYour Pick: "{game_elements[user_choice]}"')
        print(f'Computer Pick: "{game_elements[computer_choice]}"')

        
        if user_choice == computer_choice:
            draws += 1
            print("\n🤝 It's a Draw!")

        elif (
            (user_choice == 1 and computer_choice == 2)
            or (user_choice == 2 and computer_choice == 3)
            or (user_choice == 3 and computer_choice == 1)
        ):
            user_score += 1
            print("\n🎉 You Win!")

        else:
            computer_score += 1
            print("\n😔 You Lose!")

        
        print("\n------------ Score ------------")
        print(f"You       : {user_score}")
        print(f"Computer  : {computer_score}")
        print(f"Draws     : {draws}")

       
        if user_score > computer_score:
            print("\n🏆 You are currently WINNING!")
        elif user_score < computer_score:
            print("\n😔 You are currently LOSING!")
        else:
            print("\n🤝 The game is currently a DRAW!")

        # Ask if the player wants to continue
        play_again = input("\nDo you want to play again? (y/n): ").lower()

        if play_again != "y":
            break

    
    print("\n================================")
    print("           FINAL SCORE")
    print("================================")
    print(f"You       : {user_score}")
    print(f"Computer  : {computer_score}")
    print(f"Draws     : {draws}")

    if user_score > computer_score:
        print("\n🏆 Congratulations! YOU WON THE GAME!")
    elif user_score < computer_score:
        print("\n😔 Better luck next time! COMPUTER WON THE GAME!")
    else:
        print("\n🤝 The game ended in a DRAW!")

    print("\nThanks for playing! 👋")


play_game()

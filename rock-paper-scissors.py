import random

def play_rps():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("Welcome to Rock, Paper, Scissors!")
    print("Options: rock, paper, scissors")
    
    while True:
        user_choice = input("Enter your choice (or 'quit' to exit): ").lower()

        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

        computer_choice = random.choice(choices)  # Reset the computer's choice for the next round

if __name__ == "__main__":
    play_rps()

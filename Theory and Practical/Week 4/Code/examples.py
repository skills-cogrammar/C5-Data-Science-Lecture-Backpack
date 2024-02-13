import random as rd


def rock_paper_scissors(choice):
    
    games = 0
    wins = 0
    losses = 0
    
    select = ['Rock', 'Paper', 'Scissors']
    cpu_choice = rd.choice(select)

    if cpu_choice == choice:
        return f"You chose {choice}, CPU chose {cpu_choice}. It's a tie!"
    
    elif cpu_choice == 'Rock' and choice == 'Paper':
        wins += 1
        return f"You chose {choice}, CPU chose {cpu_choice}. You win!"
    
    elif cpu_choice == 'Paper' and choice == 'Scissors':
        wins += 1
        return f"You chose {choice}, CPU chose {cpu_choice}. You win!"


while True:
    user_choice = input("Please enter either Rock, Paper or Scissors : ").capitalize()
    outcome = rock_paper_scissors(user_choice)

    print(outcome)
    
    terminate = input("Go again? (Y/N) : ").upper()
    
    if terminate == 'Y':
        break
    
    elif terminate == 'N':
        continue

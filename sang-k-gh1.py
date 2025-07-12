import random  

# List of game options  
options = ["Rock", "Paper", "Scissors"]  

# Human player choice functions for each state  
human_choice_functions = {  
    1: lambda: "Rock",  # State 1: Always Rock  
    2: lambda: random.choice(options),  # State 2: Random from three options  
    3: lambda: random.choice(["Rock", "Paper"])  # State 3: Random from Rock and Paper  
}  

# Function to determine the winner  
def get_winner(human, computer):  
    if human == computer:  
        return "tie"  
    elif (human == "Rock" and computer == "Scissors") or \
         (human == "Paper" and computer == "Rock") or \
         (human == "Scissors" and computer == "Paper"):  
        return "human"  
    else:  
        return "computer"  

# Function to simulate games for a given state  
def simulate_games(state, num_games=100):  
    human_wins = 0  
    computer_wins = 0  
    ties = 0  
    
    # Select the appropriate function for the human player based on the state  
    human_choice_func = human_choice_functions[state]  
    
    # Repeat the game 100 times  
    for _ in range(num_games):  
        human_choice = human_choice_func()  # Human player's choice  
        computer_choice = random.choice(options)  # Computer's random choice  
        result = get_winner(human_choice, computer_choice)  # Determine the winner  
        
        if result == "human":  
            human_wins += 1  
        elif result == "computer":  
            computer_wins += 1  
        else:  
            ties += 1  
    
    return human_wins, computer_wins, ties  

# Run the game for each of the three states and print the results  
for state in [1, 2, 3]:  
    human_wins, computer_wins, ties = simulate_games(state)  
    print(f"State {state}:")  
    print(f"Number of human wins: {human_wins}")  
    print(f"Number of computer wins: {computer_wins}")  
    print(f"Number of ties: {ties}")  
    print()  
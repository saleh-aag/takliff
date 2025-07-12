import random  

# List of game options  
options = ["Rock", "Paper", "Scissors"]  

# Human player choice functions for each state  
human_choice_functions = {  
    1: lambda: "Rock",  # حالت 1: همیشه سنگ  
    2: lambda: random.choice(options),  # حالت 2: رندوم از سه گزینه  
    3: lambda: random.choice(["Rock", "Paper"])  # حالت 3: رندوم از سنگ و کاغذ  
}  

# Function to determine the winner  
def get_winner(human, computer):  
    if human == computer:  
        return "tie"  # مساوی  
    elif (human == "Rock" and computer == "Scissors") or \
         (human == "Paper" and computer == "Rock") or \
         (human == "Scissors" and computer == "Paper"):  
        return "human"  # بازیکن انسانی برنده  
    else:  
        return "computer"  # کامپیوتر برنده  

# Function to simulate games for a given state  
def simulate_games(state, num_games=100):  
    human_wins = 0  # تعداد بردهای بازیکن انسانی  
    
    # Select the appropriate function for the human player based on the state  
    human_choice_func = human_choice_functions[state]  
    
    # Repeat the game 100 times  
    for _ in range(num_games):  
        human_choice = human_choice_func()  # Human player's choice  
        computer_choice = random.choice(options)  # Computer's random choice  
        result = get_winner(human_choice, computer_choice)  # Determine the winner  
        
        if result == "human":  
            human_wins += 1  
    
    return human_wins  

# Run the game for each of the three states and print the results  
for state in [1, 2, 3]:  
    human_wins = simulate_games(state)  
    human_win_fraction = human_wins / 100  # کسر برد بازیکن انسانی  
    print(f"{state}:")  
    print(f"  {human_win_fraction:.2f}")  
    print()  
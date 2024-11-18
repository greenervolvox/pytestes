import random

def is_win(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True

def play():
    user = input(" choose between: 'r' for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(f'Computer choice was {computer}')
        return 'tie!'
    
    if is_win(user, computer):
        print(f'Computer choice was {computer}')
        return 'You won!' 
    
    print(f'Computer choice was {computer}')
    return 'U lost...' 
        
print(play())
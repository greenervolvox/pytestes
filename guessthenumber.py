import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0   
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} \n'))
        print(guess)
        if guess < random_number:
            print('Sorry, guess again. Too low \n')
        elif guess > random_number:
            print('Sorry, guess again. Too high \n')
    
    print(f'Got it. {random_number} \n')

guess(10)

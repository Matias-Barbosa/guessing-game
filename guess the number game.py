import random
print("********************************")
print('Welcome to "GUESS THE NUMBER!"')
print("********************************")

secretNumber = random.randint(1,10)
print('Well, I am thinking of a number between 1 and 10, you think you can guess it?')

for guessesTaken in range(7):
    print(secretNumber)
    print('Take a guess')
    guess = int(input())
    if 0 < guess < secretNumber:
        print('The secret number is higher than your shot')
        print(f'You have {6 - guessesTaken} tries left')

    elif 10 > guess > secretNumber:
        print('The secret number is lower than your shot')
        print(f'You have {6 - guessesTaken} tries left')

    elif guess > 10:
        print('Whoa hold on buddy, not so high')
        print(f'You have {6 - guessesTaken} tries left')

    elif guess < 0:
        print('I think you should try a number within the range.')
        print(f'You have {6 - guessesTaken} tries left')

    else:
        break

if guess == secretNumber:
    print("You've won the game, congratulations!")
else:
    print(f'aww the secret number was {secretNumber}, better luck next time...')

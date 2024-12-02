import random

def askforguess():
    guess = input('> ')
    if guess.isdecimal():
        return int(guess)
    print('Please enter a number between 1 and 100')

print('Guess the number by sololiqht')
print()

secret = random.randint(1,100)
print('I am thinking of a number between 1 and 100.')

for i in range(3):
    print('You have {} guesses left. Take a guess'.format(3-i))
    guess = askforguess()
    if guess == secret:
        break
    if guess>secret:
        print('Your guess is  high')
    if guess<secret:
        print('Your guess is low')

if guess == secret:
    print('Yay, you guessed my number!')
else:
    print('lol, you failed the number was',secret)

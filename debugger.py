#find bugs that keep program from working correctly
'''
There were two errors that I found. One was that the orginal code was comparing guess and toss.
This results in an error because the compiler can't compare an int value with a string value.
To resolve this, I added the coin variable. The second error was a spelling mistake of guess.
'''
import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input()
    logging.debug('guess = ' + guess)
toss = random.randint(0,1)  #0 is tails, 1 is heads
logging.debug('toss = ' + str(toss))
if toss == 0:
    coin = 'tails'
else:
    coin = 'heads'
if coin == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    #guesss = input()
    guess = input()
    if coin == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
logging.debug('End of program')

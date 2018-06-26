import sys

#function takes in one parameter and does a different mathematical equation depending on if the number is even or odd
def collatz(number):
    if number % 2 == 0:     #even
        number = number // 2
    elif number % 2 == 1:    #odd
        number = 3 * number + 1

    if number == 1:
        print(number)
        sys.exit()
    while number != 1:
        print(number)
        return collatz(number)

def main():
    print('Enter a number: ')
    try:
        userInput = int(input())
        collatz(userInput)
    except NameError:
        print('Error: must enter an integer.')

main()

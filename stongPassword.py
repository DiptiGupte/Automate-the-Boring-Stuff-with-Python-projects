import re

lengthRegex = re.compile(r'\w{8,}')
uppercaseRegex = re.compile(r'[A-Z]')
lowercaseRegex = re.compile(r'[a-z]')
numRegex = re.compile(r'[0-9]')

def stongPasswordDetection(password):
    #at least 8 characters long
    if len(password) < 8:
        return False
    #contains both uppercase and lowercase characters and has at least one digit
    if uppercaseRegex.search(password) and lowercaseRegex.search(password) and numRegex.search(password) and lengthRegex.search(password):
        return True
    else:
        return False


def main():
    print('Enter a password')
    print('(It must be at least 8 characters long,' +
            'contain both uppercase and lowercase characters' +
            'and have at least one digit)')
    password = input()
    if stongPasswordDetection(password):
        print('Strong password!')
    else:
        print('Weak password.')

main()

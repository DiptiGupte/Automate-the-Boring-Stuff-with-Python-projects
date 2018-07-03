def madLibs():
    madFile = open('givenMadLibs.txt', 'r')
    madUser = open('userMadLibs.txt', 'w')
    userInput = ''
    printToScreen = ''
    #get all words in given text
    #loop used: https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python
    with madFile as f:
        for line in f:
            for word in line.split():
                #ask user to input words and print to new text file
                if word == 'NOUN' or word == 'PRONOUN' or word == 'ADJECTIVE' or word == 'ADVERB' or word == 'VERB':
                    print('Enter a ' + word.lower() + ':')
                    userInput = input()
                    madUser.write(userInput)
                    madUser.write(' ')
                    printToScreen += userInput + ' '
                else:
                    madUser.write(word)
                    madUser.write(' ')
                    printToScreen += word + ' '
    print(printToScreen)
    madUser.close()

madLibs()

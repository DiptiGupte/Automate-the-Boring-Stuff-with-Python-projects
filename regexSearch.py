import re, os

#opens all .txt files in a folder
#searches for any line that matches a user-supplied regular expression
#prints results to sceen
def regexSearch():
    print('What expression are you looking for?')
    print('(If you want to look for more than one thing seperate each word with |. e.g. word1|word2|)')
    expression = input()
    #panda|NOUN|the
    regexExpression = re.compile(r'\b' + expression + '\b')
    #loop used: https://stackoverflow.com/questions/1124810/how-can-i-find-path-to-given-file
    for r,d,f in os.walk('/Users/diptigupte/Desktop/GitHub/Automate-the-Boring-Stuff-with-Python-projects'):
        for files in f:
            if files.endswith('.txt'):
                print(os.path.join(r, files))
                currentText = os.path.join(r, files)
                text = open(currentText, 'r')
                with text as t:
                    for line in t:
                        find = regexExpression.findall(line)    #searches line by line of text for expression
                        if len(find) > 0:   #if find is not empty ([]) then it prints what it found
                            print(find)
            else:
                continue

regexSearch()

#function that takes a list value as an argument
#returns a string with all the items separated by a comma and a space, with and inserted before the last item
def comma(list):
    commaStr = ''
    for i in range(len(list)):
        if i == 0:
            commaStr = list[i]
        elif i == len(list) - 1:
            commaStr = commaStr + ', and ' + list[i]
        else:
            commaStr = commaStr + ', ' + list[i]
    return commaStr

def main():
    commaList = []
    while True:
        print('Enter an item for index ' + str(len(commaList) + 1) +
            " (or enter 'done' to stop): ")
        userInput = str(input())
        if userInput == 'done':
            break
        commaList.append(userInput)
    #print(commaList)
    string = comma(commaList)
    print(string)

main()

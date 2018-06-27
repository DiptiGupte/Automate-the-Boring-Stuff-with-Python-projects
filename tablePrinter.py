#finds longest string and returns the length
def longestStr(aList):
    longest = 0
    for i in aList:
        if len(i) > longest:
            longest = len(i)
    return longest

#finds biggest int in list and returns it
def biggestInt(aList):
    biggest = 0
    for i in aList:
        if i > biggest:
            biggest = i
    return biggest

#takes a list of list of strings
#displays it in well-organized table with each column right-justified
def printTable(table):
    #find the longest string within each inner list
    colWidths = [0] * len(table)
    for i in range(len(colWidths)):
        colWidths[i] = longestStr(table[i])
        i += 1
    #find largest value in the colWidths list
    width = biggestInt(colWidths)
    #print table
    row = ''
    for j in range(len(tableData[0])):
        for k in range(len(tableData)):
            row += table[k][j].rjust(width)
        print row
        row = ''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)

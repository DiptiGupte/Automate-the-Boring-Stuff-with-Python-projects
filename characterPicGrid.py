#print out grid
def printGrid(grid):
    columns = len(grid)
    rows = len(grid[0])
    temp = ''
    for i in range(rows):
        for j in range(columns):
            temp += grid[j][i] + ' '
        print(temp)
        temp = ''

def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'o', 'o', '.', '.', '.'],
            ['o', 'o', 'o', 'o', '.', '.'],
            ['o', 'o', 'o', 'o', 'o', '.'],
            ['.', 'o', 'o', 'o', 'o', 'o'],
            ['o', 'o', 'o', 'o', 'o', '.'],
            ['o', 'o', 'o', 'o', '.', '.'],
            ['.', 'o', 'o', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    printGrid(grid)

main()

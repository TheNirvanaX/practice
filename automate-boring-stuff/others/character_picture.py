#this program prints "charcter picture grid"
grid = [['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'], 
    ['.', '.', '.', '.', '.', '.']]

width = len(grid)
height = len(grid[0])
#print loop
for y in range(height):
    for x in range(width):
        print(grid[x][y],end='')
    print()
# with open("countries.txt", "r") as countries:
#     total = 0
#     for line in countries:
#         total += len(line.split())
#     print(total/149)

from pprint import pprint

def print_grid(grid):
    for row in grid:
        for e in row:
            print(e, end=" "),
        print()

def get_neighbors(x, y):
    return [[x-1,y], [x+1,y], [x, y-1], [x, y+1]]

def get_inhabited(grid):
    inhab = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                inhab.append([i,j])
    return inhab

grid = [[0 for i in range(12)] for i in range(12)]
grid[6][6] = 1
for i in range(20):
    inhabited = get_inhabited(grid)
    for j in inhabited:
        grid[j[0]][j[1]] = 2
    for x in inhabited:
        for y in get_neighbors(x[0], x[1]):
            if y not in inhabited:
                grid[y[0]][y[1]] = 1
                grid[x[0]][x[1]] = 1
    print(len(get_inhabited(grid)))
    #print_grid(grid)

print_grid(grid)
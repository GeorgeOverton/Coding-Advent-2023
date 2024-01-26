def visibleTrees():
    file = open('treehouse.txt')
    lookdown = []
    lookup = []
    lookleft = []
    lookright = []
    grid = []
    vis = 0
    dupe = 0
    for line in file:
        lines = Convert(line)
        if "\n" in lines:
            lines.remove("\n")
        grid.append(lines)
    for i in range(len(grid)):
        lookright.append(0)
        for j in range(0, len(grid[i])-1,1):
            if int(grid[i][j]) > int(lookright[i]):
                lookright[i] = grid[i][j]
                vis += 1
                grid[i][j] = "null" + grid[i][j]
    for i in range(0,len(grid)-1,1):
        lookleft.append(0)
        for j in range(0, len(grid[i])-1 ,1):
            pos = len(grid[i])-1-j
            if grid[i][pos][:4] == "null":
                lookleft[i] = int(grid[i][j][4:])
            elif int(grid[i][pos]) > int(lookleft[i]):
                lookleft[i] = grid[i][j]
                vis += 1
                grid[i][j] = "null" + grid[i][j]
    for i in range(0,len(grid[i-1])-1,1):
        lookdown.append(0)
        for j in range(0,len(grid)-1,1):
            if grid[j][i][:4] == "null":
                lookdown[i] = int(grid[j][i][4:])
            elif int(grid[j][i]) > int(lookdown[i]):
                lookdown[i] = grid[j][i]
                vis += 1
                grid[j][i] = "null" + grid[j][i]
    for i in range(0,len(grid[1])-1,1):
        lookup.append(0)
        for j in range(len(grid)-1, 0 ,1):
            if grid[i][j][:4] == "null":
                lookup[i] = int(grid[j][i][4:])
            elif int(grid[j][i]) > int(lookup[i]):
                lookup[i] = grid[j][i]
                vis += 1
                grid[j][i] = "null" + grid[j][i]
    print(lookdown)
    print(lookup)
    print(lookleft)
    print(lookright)
    print(vis)


def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


visibleTrees()

f = open("data.txt", "r")


data = []
for line in f:
    linechars = []
    for char in line:
        if char == '\n':
            continue
        linechars.append(char)
    data.append(linechars)

visited = {}

def in_bounds(coord):
    return len(data) > coord[0] >= 0 and len(data[0]) > coord[1] >= 0

def dfs(x, y):
    stack = [(x,y)]
    visited[(x,y)] = 1
    move_x = [1,0,-1,0]
    move_y = [0,1,0,-1]
    area = 0
    perimeter = 0
    fences = [{},{},{},{}]
    while len(stack) != 0:
        top_x, top_y = stack.pop()
        area = area + 1
        for i in range(4):
            future_x = top_x + move_x[i]
            future_y = top_y + move_y[i]
            if not in_bounds((future_x, future_y)):
                perimeter = perimeter + 1
                fences[i][(future_x, future_y)] = 1
                continue
            if data[future_x][future_y] != data[top_x][top_y]:
                perimeter = perimeter + 1
                fences[i][(future_x, future_y)] = 1
            elif (future_x, future_y) not in visited:
                stack.append((future_x, future_y))
                visited[(future_x, future_y)] = 1
    
    sides = 0
    for i in range(4):
        fencemap = fences[i]
        minx = 10**9
        maxx = 0
        miny = 10**9
        maxy = 0
        for fence in fencemap:
            if fence[0] > maxx:
                maxx = fence[0]
            if fence[0] < minx:
                minx = fence[0]
            if fence[1] > maxy:
                maxy = fence[1]
            if fence[1] < miny:
                miny = fence[1]
        
        for x in range(minx, maxx+1):
            for y in range(miny, maxy+1):
                if (x,y) in fencemap:
                    if i % 2 == 0:
                        if (x,y+1) not in fencemap:
                            sides = sides + 1
                    else:
                        if (x+1, y) not in fencemap:
                            sides = sides + 1

    return(area, perimeter, sides)


price = 0
bulk_price = 0
for width in range(len(data)):
    for height in range(len(data[0])):
        if (width, height) not in visited:
            costs = dfs(width, height)
            price = price + costs[0] * costs[1]
            bulk_price = bulk_price + costs[0] * costs[2]
print(f"total price of fencing = {price}")
print(f"total price of fencing if bought in bulk = {bulk_price}")

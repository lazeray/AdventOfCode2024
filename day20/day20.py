f = open("data.txt", "r")

def in_bounds(x, y):
    return len(data) > x >= 0 and len(data[0]) > y >= 0

def dist_to_point(point):
    stack = [(point, 0)]
    dist = {}
    FLOOD_X = [1,-1,0,0]
    FLOOD_Y = [0,0,1,-1]


    while stack:
        top = stack.pop()
        dist[top[0]] = top[1]
        for i in range(4):
            new_location = (top[0][0] + FLOOD_X[i], top[0][1] + FLOOD_Y[i])
            if new_location not in dist and data[new_location[0]][new_location[1]] != '#':
                stack.insert(0, (new_location, top[1] + 1))
    return dist


data = []
x = 0

for line in f:
    line_list = []
    line = line.rstrip("\n")
    for char in line:
        line_list.append(char)
        y = line.find("E")
        if y != -1:
            end = (x, y)
        y = line.find("S")
        if y != -1:
            start = (x, y)
    x = x + 1
    data.append(line_list)

data[start[0]][start[1]] = '.'
data[end[0]][end[1]] = '.'

dist_to_end = dist_to_point(end)
dist_to_start = dist_to_point(start)

HACK_X = [-2,-1,0,1,2,1,0,-1]
HACK_Y = [0,-1,-2,-1,0,1,2,1]

regular_length = dist_to_end[start]


numsaves = 0

for x in range(len(data)):
    for y in range(len(data[0])):
        for diff_x in range(-20, 21):
            for diff_y in range(abs(diff_x) - 20, 21 - abs(diff_x)):
                hacked_x = x + diff_x
                hacked_y = y + diff_y
                if in_bounds(hacked_x, hacked_y) and data[hacked_x][hacked_y] == '.' and data[x][y] == '.':
                    hacked_length = dist_to_start[(x,y)] + dist_to_end[(hacked_x, hacked_y)] + abs(diff_x) + abs(diff_y)
                    diff = regular_length - hacked_length
                    if diff >= 100:
                        numsaves = numsaves + 1

print(numsaves)
import heapq
def get_new_dirs(dir):
    if dir == (0,1) or dir == (0,-1):
        return [(-1,0),(1,0)]
    if dir == (1,0) or dir == (-1,0):
        return [(0,-1),(0,1)]    

def is_node(x, y, currdir):
    new_dirs = get_new_dirs(currdir)
    if data[x + new_dirs[0][0]][y + new_dirs[0][1]] != '#':
        return True
    if data[x + new_dirs[1][0]][y + new_dirs[1][1]] != '#':
        return True
    return False

f = open("data.txt", "r")
data = []
for line in f:
    line = line.rstrip("\n")
    line = list(line)
    data.append(line)

visited = {}
viewspots = {}

pq = [] # start
pq.append((-1, len(data) - 2, 0, (0,1),[(len(data)-2, 0)])) # very scuffed
heapq.heapify(pq)

print(len(data)-2, 1)
FLOOD_X = [1,-1,0,0]
FLOOD_Y = [0,0,1,-1]
minscore = 10000000
while pq:
    top = heapq.heappop(pq) # score, x, y, dir, path make sure pq is actually a priority queue sorted by score!
    dir = top[3]
    next_x = top[1] + dir[0]
    next_y = top[2] + dir[1]
    path = top[4]
    score = top[0]
    if (next_x, next_y, dir) in visited and score != visited[(next_x, next_y, dir)]:
        continue
    visited[(next_x, next_y, dir)] = score
    score = score + 1

    end = False
    while not is_node(next_x, next_y, dir):
        next_x = next_x + dir[0]
        next_y = next_y + dir[1]
        score = score + 1
        if data[next_x][next_y] == 'E':
            #print(f"lowest raindeer score = {score}")
            path.append((next_x, next_y))
            if score <= minscore:
                for index in range(1, len(path)-1):
                    x1 = path[index][0]
                    y1 = path[index][1]
                    x2 = path[index+1][0]
                    y2 = path[index+1][1]
                    if x1 != x2:
                        if x1 < x2:
                            for x in range(x1, x2 + 1):
                                viewspots[(x, y1)] = 1
                        else:
                            for x in range(x2, x1 + 1):
                                viewspots[(x, y1)] = 1
                    else:
                        if y1 < y2:
                            for y in range(y1, y2+1):
                                viewspots[(x1, y)] = 1
                        else:
                            for y in range(y2, y1+1):
                                viewspots[(x1, y)] = 1

                minscore = score
        if data[next_x][next_y] == '#': # dead end
            next_x = next_x - dir[0]
            next_y = next_y - dir[1]
            break
    newpath = path + [(next_x, next_y)]
    
    for newdir in get_new_dirs(dir):
        if data[next_x + newdir[0]][next_y + newdir[1]] != '#':
            heapq.heappush(pq, (score + 1000, next_x, next_y, newdir, newpath))
    if data[next_x + dir[0]][next_y + dir[1]] != '#':
        heapq.heappush(pq, (score, next_x, next_y, dir, newpath))

print(len(viewspots))
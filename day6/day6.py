def get_next_dir(dir):
    if dir[0] == 0 and dir[1] == 1:
        return (1,0)
    if dir[0] == 1 and dir[1] == 0:
        return (0,-1)
    if dir[0] == 0 and dir[1] == -1:
        return (-1,0)
    if dir[0] == -1 and dir[1] == 0:
        return (0,1)

def is_out_of_bounds(x, y):
    if len(maze) > x >= 0 and len(maze[0]) > y >= 0:
        return False
    return True

def has_loop(position, dir):
    loop_visited = {}
    while True:
        if position in loop_visited:
            for prev_dir in loop_visited[position]:
                if dir == prev_dir:
                    return True
            loop_visited[position].append(dir)
        else:
            loop_visited[position] = [dir]
        future_x = dir[0] + position[0]
        future_y = dir[1] + position[1]
        if is_out_of_bounds(future_x, future_y):
            break
        if maze[future_x][future_y] == '#':
            dir = get_next_dir(dir)
        else:
            position = (position[0] + dir[0], position[1] + dir[1])
    return False

f = open("data.txt", "r")

maze = []
for line in f:
    #print(line)
    char_line = []
    for char in line:
        char_line.append(char)
    maze.append(char_line)



for row_index, row in enumerate(maze): # finds position of the guard
    for col_index, char in enumerate(row):
        if char == '^':
            initial_position = (row_index, col_index)

dir = (-1,0)
visited = {}

position = initial_position
while True: # assumes the guard will eventually exit

    visited[position] = dir
    future_x = dir[0] + position[0]
    future_y = dir[1] + position[1]
    if is_out_of_bounds(future_x, future_y):
        break
    if maze[future_x][future_y] == '#':
        dir = get_next_dir(dir)
    position = (position[0] + dir[0], position[1] + dir[1])

num_obstruction_spots = 0

for position in visited:
    if position == initial_position:
        continue
    maze[position[0]][position[1]] = '#'
    if has_loop(initial_position, dir):
        num_obstruction_spots = num_obstruction_spots + 1
    maze[position[0]][position[1]] = '.'


print(f"number of unique tiles visited: {len(visited)}")
print(f"number of valid obstruction spots = {num_obstruction_spots}")


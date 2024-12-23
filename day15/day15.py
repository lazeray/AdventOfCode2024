f = open("data.txt", "r")


is_maze = True
data_array = []
wide_data = []
commands_array = []
start = [0,0]
newstart = [0,0]
x = 0
for line in f:
    if line == "\n":
        is_maze = False
    else:
        line = line.rstrip("\n")
        if is_maze:
            newline = ""
            for char in line:
                if char == '#':
                    newline = newline + '##'
                elif char == 'O':
                    newline = newline + '[]'
                elif char == '@':
                    newline = newline + '@.'
                elif char == ".":
                    newline = newline + '..'
            y = line.find("@")
            if y != -1:
                start[0] = x
                start[1] = y
            y = newline.find("@")
            if y != -1:
                newstart[0] = x
                newstart[1] = y
            data_array.append(list(line))
            wide_data.append(list(newline))            
            x = x + 1
        else:
            commands_array.extend(list(line))
# goal : 9021
for command in commands_array:
    if command == '^':
        dir = [-1,0]
    elif command == '>':
        dir = [0,1]
    elif command == '<':
        dir = [0,-1]
    elif command == 'v':
        dir = [1,0]
    next_x = start[0] + dir[0]
    next_y = start[1] + dir[1]
    while data_array[next_x][next_y] == 'O':
        next_x = next_x + dir[0]
        next_y = next_y + dir[1]
    if data_array[next_x][next_y] != '#':
        data_array[next_x][next_y] = 'O'
        data_array[start[0]][start[1]] = '.'
        start[0] = start[0] + dir[0]
        start[1] = start[1] + dir[1]
        data_array[start[0]][start[1]] = '@'
print(newstart)

for commandnum, command in enumerate(commands_array):
    if command == '^' or command == 'v':
        if command == '^':
            dir = [-1,0]
        else:
            dir = [1,0]
        next_x = newstart[0] + dir[0]
        next_y = newstart[1] + dir[1]
        boxmap = []
        tempmap = []
        if wide_data[next_x][next_y] == '#':
            continue
        if wide_data[next_x][next_y] == '[':
            tempmap.append((next_x, next_y))
        elif wide_data[next_x][next_y-1] == '[':
            tempmap.append((next_x, next_y-1))        
        stop = False
        while tempmap: # while tempmap not empty
            top = tempmap.pop()
            boxmap.insert(0, top)
            if wide_data[top[0]+dir[0]][top[1]-1] == '[':
                tempmap.insert(0,(top[0]+dir[0], top[1]-1))
            if wide_data[top[0]+dir[0]][top[1]] == '[':
                tempmap.insert(0,(top[0]+dir[0], top[1]))
            if wide_data[top[0]+dir[0]][top[1]+1] == '[':
                tempmap.insert(0,(top[0]+dir[0], top[1]+1))
            if wide_data[top[0]+dir[0]][top[1]] == '#':
                stop = True
                break
            if wide_data[top[0]+dir[0]][top[1]+1] == '#':
                stop = True
                break
        if stop == False:
            for box in boxmap:
                wide_data[box[0] + dir[0]][box[1]] = '['
                wide_data[box[0] + dir[0]][box[1] + 1] = ']'
                wide_data[box[0]][box[1]] = '.'
                wide_data[box[0]][box[1] + 1] = '.'
            wide_data[newstart[0]][newstart[1]] = '.'
            newstart[0] = newstart[0] + dir[0]
            newstart[1] = newstart[1] + dir[1]
            wide_data[newstart[0]][newstart[1]] = '@'
           
        
    elif command == '<' or command == '>':
        if command == '<':
            dir = [0,-1]
        else:
            dir = [0,1]
        next_x = newstart[0] + dir[0]
        next_y = newstart[1] + dir[1]

        while wide_data[next_x][next_y] == '[' or wide_data[next_x][next_y] == ']':
            next_x = next_x + dir[0]
            next_y = next_y + dir[1]
        if wide_data[next_x][next_y] != '#':
            while next_x != newstart[0] or next_y != newstart[1]:
                wide_data[next_x][next_y] = wide_data[next_x - dir[0]][next_y - dir[1]]
                next_x = next_x - dir[0]
                next_y = next_y - dir[1]
            wide_data[newstart[0]][newstart[1]] = '.'
            newstart[0] = newstart[0] + dir[0]
            newstart[1] = newstart[1] + dir[1]
    
        

wide_coords = 0
sum_coords = 0
for x, col in enumerate(data_array):
    for y, char in enumerate(col):
        if char == 'O':
            sum_coords = sum_coords + 100*x + y



for x, col in enumerate(wide_data):
    for y, char in enumerate(col):
        print(char, end="")
        if char == '[':
            wide_coords = wide_coords + 100*x + y
    print()

print(f"Sum of all box coords = {sum_coords}")
print(f"Sum of all wide coords = {wide_coords}")
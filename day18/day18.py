BOARD_SIZE = 71

def in_bounds(x, y):
    return BOARD_SIZE > x >= 0 and BOARD_SIZE > y >= 0

def has_path(blocks):
    board = [['.'] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    for block in blocks:
        board[block[1]][block[0]] = '#'

    stack = [(0,0,0)]
    visited = {}


    FLOOD_X = [1,-1,0,0]
    FLOOD_Y = [0,0,1,-1]

    while stack:
        top = stack.pop()
        if top[0] == BOARD_SIZE-1 and top[1] == BOARD_SIZE-1:
            return True


        for i in range(4):
            new_x = top[0] + FLOOD_X[i]
            new_y = top[1] + FLOOD_Y[i]
            new_length = top[2] + 1
            if in_bounds(new_x, new_y) and (new_x, new_y) not in visited and board[new_x][new_y] != '#':
                visited[(new_x, new_y)] = 1 
                stack.insert(0, (new_x, new_y, new_length))
            
    return False

blocks = []

f = open("data.txt")
for line in f:
    x = int(line.split(',')[0])
    y = int(line.split(',')[1])
    blocks.append((x,y))
    
# minblocks = 0
# maxblocks = len(blocks) - 1
# while maxblocks - minblocks != 1:
#     if has_path(blocks[:int((maxblocks-minblocks)/2)]):
#         minblocks = int((maxblocks+minblocks)/2)
#     else:
#         maxblocks = int((maxblocks+minblocks)/2)
# print(blocks[minblocks])

for i in range(len(blocks)):
    if has_path(blocks[:i]) == False:
        print(blocks[i-1])
        break
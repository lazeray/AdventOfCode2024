def search_string(x, y, target_string):
    search_x = [-1,0,1,-1,1,-1,0,1]
    search_y = [-1,-1,-1,0,0,1,1,1]

    count = 0

    for dir_x, dir_y in zip(search_x, search_y):
        is_target = True
        temp_x = x
        temp_y = y
        for index in range(len(target_string)):
            if not is_accurate(temp_x, temp_y, target_string[index]):
                is_target = False
                break
            temp_x = temp_x + dir_x
            temp_y = temp_y + dir_y
        if is_target:
            count = count + 1
    return count

def search_x(x, y):
    search_m_1 = [[1,1],[-1,1],[-1,-1],[1,-1]]
    search_m_2 = [[-1,1],[-1,-1],[1,-1],[1,1]]

    count = 0

    for m_1, m_2 in zip(search_m_1, search_m_2):
        if not is_accurate(x, y, 'A'):
            continue
        if not (is_accurate(x + m_1[0], y + m_1[1], 'M') and is_accurate(x - m_1[0], y - m_1[1], 'S')):
            continue
        if not (is_accurate(x + m_2[0], y + m_2[1], 'M') and is_accurate(x - m_2[0], y - m_2[1], 'S')):
            continue
        count = count + 1
    return count

def is_accurate(x, y, char):
    if len(text_array) > x >= 0 and len(text_array[0])-1 > y >= 0: # in bounds
        if text_array[x][y] == char:
            return True
    return False

f = open("data.txt", "r")

text_array = []
for line in f:
    text_array.append(line) # converts into a 2d array


total_XMAS = 0
total_X_MAS = 0
for x in range(len(text_array)):
    for y in range(len(text_array[0])):
        total_XMAS = total_XMAS + search_string(x, y, "XMAS")
        total_X_MAS = total_X_MAS + search_x(x, y)

print(f"Total XMAS count = {total_XMAS}")
print(f"Total X-MAS count = {total_X_MAS}")
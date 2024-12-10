f = open("data.txt", "r")

data = []
for line in f:
    chars = []
    for char in line:
        if char != '\n':
            chars.append(char)
    data.append(chars)


def in_bounds(x,y):
    return (len(data) > x >=0) and (len(data[0]) > y >= 0)

def trailhead_score(x, y, char):
    if char == '9':
        return [(x,y)]
    targetchar = chr(ord(char) + 1)
    my_map = {}
    flood =[(1,0),(-1,0),(0,1),(0,-1)]
    for index in range(4):
        futurex = x + flood[index][0]
        futurey = y + flood[index][1]
        if in_bounds(futurex,futurey) == True:
            if data[futurex][futurey] != targetchar:
                continue
            for el in trailhead_score(futurex,futurey,targetchar):
                my_map[el] = 1
    return my_map


def trailhead_rating(x, y, char):
    if char == '9':
        return 1
    targetchar = chr(ord(char) + 1)
    my_rating = 0
    flood =[(1,0),(-1,0),(0,1),(0,-1)]
    for index in range(4):
        futurex = x + flood[index][0]
        futurey = y + flood[index][1]
        if in_bounds(futurex,futurey) == True:
            if data[futurex][futurey] != targetchar:
                continue
            my_rating = my_rating +  trailhead_rating(futurex,futurey,targetchar)
    return my_rating



total_trailhead_score = 0
total_trailhead_rating = 0

for x, line in enumerate(data):
    for y, char in enumerate(line):
        total_map = {}
        if char == '0':
            for el in trailhead_score(x, y, char):
                total_map[el] = 1
            total_trailhead_score = total_trailhead_score + len(total_map)
            total_trailhead_rating = total_trailhead_rating + trailhead_rating(x, y, char)

print(f"total trailhead score: {total_trailhead_score}")
print(f"total trailhead rating: {total_trailhead_rating}")
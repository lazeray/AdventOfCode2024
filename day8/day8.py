def in_bounds(coord):
    height = coord[0]
    width = coord[1]
    return max_height > height >= 0 and max_width > width >= 0

f = open("data.txt", "r")


max_height = 0
max_width = 0

antennae_map = {}
for height, line in enumerate(f):
    max_height = max_height + 1 # probably some more elegant way of doing this
    max_width = len(line)
    for width, char in enumerate(line):
        if char != '.' and char != '\n':
            if char in antennae_map:
                antennae_map[char].append((height, width))
            else:
                antennae_map[char] = [(height,width)]

antinode_map = {} 
harmonic_antinode_map = {}
for antennae in antennae_map.values():

    for i in range(len(antennae)):
        for z in range(i):
            diff_height = antennae[i][0] - antennae[z][0]
            diff_width = antennae[i][1] - antennae[z][1]
            coord1 = ((antennae[i][0] + diff_height), (antennae[i][1] + diff_width))
            coord2 = ((antennae[z][0] - diff_height), (antennae[z][1] - diff_width))
            if in_bounds(coord1) and coord1 not in antinode_map:
                antinode_map[coord1] = 1
            if in_bounds(coord2) and coord2 not in antinode_map:
                antinode_map[coord2] = 1
            
            coord = antennae[i]
            while in_bounds(coord):
                if in_bounds(coord) and coord not in harmonic_antinode_map:
                    harmonic_antinode_map[coord] = 1
                coord = ((coord[0] + diff_height), (coord[1] + diff_width))
            coord = antennae[z]
            while in_bounds(coord):
                if in_bounds(coord) and coord not in harmonic_antinode_map:
                    harmonic_antinode_map[coord] = 1
                coord = ((coord[0] - diff_height),(coord[1] - diff_width))


print(f"total unique antinnodes: {len(antinode_map)}")
print(f"total unique antinnodes with harmonics: {len(harmonic_antinode_map)}")
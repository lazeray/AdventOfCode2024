f = open("data.txt", "r")
list_one = []
list_two = []

for line in f: # parses data
    values = line.split()
    list_one.append(int(values[0]))
    list_two.append(int(values[1]))

list_one.sort()
list_two.sort()

total_diff = 0
total_sim = 0


for index in range(len(list_one)): # pt1
    diff = abs(list_one[index] - list_two[index])
    total_diff = total_diff + diff

for value_one in list_one: # pt2
    sim_count = 0
    for value_two in list_two: 
        if value_one == value_two:
            sim_count = sim_count + 1
    sim = sim_count * value_one
    total_sim = total_sim + sim

print(f"total diff: {total_diff}")
print(f"total similarity score: {total_sim}")


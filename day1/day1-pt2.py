f = open("data.txt", "r")
list_one = []
list_two = []

for line in f:
    values = line.split()
    list_one.append(int(values[0]))
    list_two.append(int(values[1]))

total_sim = 0

for value_one in list_one:
    sim_count = 0
    for value_two in list_two:
        if value_two == value_one:
            sim_count = sim_count + 1
    sim = sim_count * value_one
    total_sim = total_sim + sim

print(f"total similarity score: {total_sim}")


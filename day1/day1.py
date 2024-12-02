f = open("data.txt", "r")
list_one = []
list_two = []

for line in f:
    values = line.split()
    list_one.append(int(values[0]))
    list_two.append(int(values[1]))

list_one.sort()
list_two.sort()

total_diff = 0

for index in range(len(list_one)):
    diff = abs(list_one[index] - list_two[index])
    total_diff = total_diff + diff

print(f"total diff: {total_diff}")
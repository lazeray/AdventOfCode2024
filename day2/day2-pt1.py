f = open("data.txt", "r")

total_safe = 0

for line in f:
    values = line.split() # splits into strings
    values = [int(value) for value in values] # converts all strings into ints
    
    is_increasing = True
    is_decreasing = True
    prev_val = values[0]
    for index in range(1, len(values)):
        value = values[index]
        if prev_val - value == 0:
            is_increasing = False
            is_decreasing = False
            break
        if prev_val - value > 3 or prev_val - value < 1:
            is_increasing = False
        if prev_val - value < -3 or prev_val - value > -1:
            is_decreasing = False
        prev_val = value
    
    if is_increasing or is_decreasing:
        total_safe = total_safe + 1

print(f"total safe reports: {total_safe}")
    

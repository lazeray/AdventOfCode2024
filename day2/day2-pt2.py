import copy

def is_safe(values):
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
    
    return is_increasing or is_decreasing



f = open("data.txt", "r")

total_safe = 0

for line in f:
    values = line.split() # splits into strings
    values = [int(value) for value in values] # converts all strings into ints
    
    if is_safe(values):
        total_safe = total_safe + 1
    else:
        for index in range(len(values)):
            modified_values = values[:index] + values[index + 1:]
            if is_safe(modified_values):
                total_safe = total_safe + 1
                break

print(f"total safe reports: {total_safe}")
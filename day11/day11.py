f = open("data.txt", "r")
for line in f:
    values = line.split()

dp = {}
def sol(value, depth):
    if depth == 0:
        return 1
    if (value, depth) in dp:
        return dp[(value, depth)]
    values = []
    if int(value) == 0:
        values = ["1"]
    elif len(value) % 2 == 0:
        values = [str(int(value[0:int(len(value)/2)])), str(int(value[int(len(value)/2):]))]
    else:
        values = [str(int(value)*2024)]
    result = 0
    for new_val in values:
        result = result + sol(new_val, depth -1)
    dp[(value, depth)] = result
    return result


total_stones = 0
for value in values:
    total_stones = total_stones + sol(value, 75)


print(f"total stones = {total_stones}")
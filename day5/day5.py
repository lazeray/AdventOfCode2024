f = open("data.txt", "r")


instructions = []

is_instruction = True

correct_order_sum = 0
invalid_order_sum = 0

for line in f:

    if line == "\n":
        is_instruction = False # move on to next section
        continue
    if is_instruction:
        num1 = int(line[:2])
        num2 = int(line[3:5])
        instructions.append([num1, num2])
    else:
        is_valid_sequence = True
        invalid_middle = 0

        values = list(map(int, line.split(","))) # creates array of ints
        for index_outer in range(len(values)):
            before = 0
            expected_before = 0
            for value in values:
                if [value, values[index_outer]] in instructions:
                    expected_before = expected_before + 1

            for index_inner in range(index_outer):
                if [values[index_inner], values[index_outer]] in instructions:
                    before = before + 1
            if before != expected_before:
                is_valid_sequence = False
            if expected_before == int(len(values)/2):
                invalid_middle = values[index_outer]
        if is_valid_sequence:
            correct_order_sum = correct_order_sum + values[int(len(values)/2)]
        else:
            invalid_order_sum = invalid_order_sum + invalid_middle
print(f"Sum of middle page numbers = {correct_order_sum}")
print(f"Sum of middle page numbers of invalid orders = {invalid_order_sum}")
            


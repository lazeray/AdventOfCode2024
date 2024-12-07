def generate_operations(numops, length):
    operations = []
    if length == 0:
        return [""]
    for i in range(numops):
        for operation in generate_operations(numops, length-1):
            operations.append(str(i) + operation)
    return operations

f = open("data.txt", "r")

true_eq_sum = 0
true_new_sum = 0

for line in f:
    values = line.split()
    target = int(values[0][:-1])
    operands = [int(x) for x in values[1:]]
    operations_array = generate_operations(2, len(operands)-1)
    for operations in operations_array: # part 1
        quotient = operands[0]
        for index, char in enumerate(operations):
            if char == '0':
                quotient = quotient + operands[index+1]
            if char == '1':
                quotient = quotient * operands[index+1]
        if quotient == target:
            true_eq_sum = true_eq_sum + quotient
            break
    
    operations_array = generate_operations(3, len(operands)-1)
    for operations in operations_array: # part 1
        quotient = operands[0]
        for index, char in enumerate(operations):
            if char == '0':
                quotient = quotient + operands[index+1]
            if char == '1':
                quotient = quotient * operands[index+1]
            if char == '2':
                quotient = int(str(quotient) + str(operands[index+1]))
        if quotient == target:
            true_new_sum = true_new_sum + quotient
            break


print(f"Total calibration result = {true_eq_sum}")
print(f"Total calibration result with concat = {true_new_sum}")
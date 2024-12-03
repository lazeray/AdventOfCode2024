f = open("data.txt", "r")

mult_sum = 0

do = True

enabled_mult_sum = 0

for line in f:
    currstring = ""
    index = 0
    while True:
        if index + 4 <= len(line) and line[index:index+4] == "do()":
            do = True
        if index + 7 <= len(line) and line[index:index+7] == "don't()":
            do = False
        if index + 4 <= len(line) and line[index:index+4] != "mul(":
            index = index + 1
            continue
        index = index + 4
        
        num1 = ""
        while index < len(line) and line[index].isdigit():
            num1 = num1 + line[index]
            index = index + 1
        
        if index < len(line) and line[index] != ',':
            index = index + 1
            continue
        index = index + 1

        num2 = ""
        while index < len(line) and line[index].isdigit():
            num2 = num2 + line[index]
            index = index + 1
        
        if index < len(line) and line[index] != ')':
            index = index + 1
            continue
        index = index + 1
        if index > len(line):
            break

        if len(num1) > 0 and len(num2) > 0:
            mult = int(num1)*int(num2)
            if do:
                enabled_mult_sum = enabled_mult_sum + mult
            mult_sum = mult_sum + mult
print(f"Result of multiplications = {mult_sum}")
print(f"Result of multiplications  with do's and don'ts = {enabled_mult_sum}")
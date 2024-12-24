def immgen(operand, is_literal):
    if is_literal:
        return operand
    else:
        if 3 >= operand >= 0:
            return operand
        else:
            return registers[operand-4]

def binary_converter(num):
    if num == 0:
        return "000"
    if num == 1:
        return "001"
    if num == 2:
        return "010"
    if num == 3:
        return "011"
    if num == 4:
        return "100"
    if num == 5:
        return "101"
    if num == 6:
        return "110"
    if num == 7:
        return "111"

def decimal_converter(bin):
    if bin == "000":
        return 0
    if bin == "001":
        return 1
    if bin == "010":
        return 2
    if bin == "011":
        return 3
    if bin == "100":
        return 4
    if bin == "101":
        return 5
    if bin == "110":
        return 6
    if bin == "111":
        return 7
    

registers = [46337277,0,0]
pc = 0

f = open("data.txt", "r") # honestly just changing input data since i cba data parsing

output = []
visited = {}

# 0,3,5,4,3,0, sol = 117440

a = "00000000"


for line in f:
    commands = line.split(",")
    commands = [int(x) for x in commands]
    pc = 0
    output = []
    while pc < len(commands):
        if (tuple(registers), pc) in visited:
            break
        visited[(tuple(registers), pc)] = 1 # check for loops
        opcode = commands[pc] # fetch!!!
        operand = commands[pc+1]
        pc = pc + 2

        if opcode == 0:
            imm = immgen(operand, False)
            num = registers[0]
            denom = pow(2, imm)
            registers[0] = int(num / denom)
        elif opcode == 1:
            imm = immgen(operand, True)
            registers[1] = registers[1] ^ imm
        elif opcode == 2:
            imm = immgen(operand, False)
            registers[1] = imm % 8
        elif opcode == 3:
            imm = immgen(operand, True)
            if registers[0] != 0:
                pc = imm
        elif opcode == 4:
            registers[1] = registers[1] ^ registers[2]
        elif opcode == 5:
            imm = immgen(operand, False)
            output.append(imm % 8)
        elif opcode == 6:
            imm = immgen(operand, False)
            num = registers[0]
            denom = pow(2, imm)
            registers[1] = int(num / denom)
        elif opcode == 7:
            imm = immgen(operand, False)
            num = registers[0]
            denom = pow(2, imm)
            registers[2] = int(num / denom)
    
    solutions = [("00000000", len(commands) - 1)]
    while solutions:
        top = solutions.pop()
        goal = commands[top[1]]
        a = top[0]
        if top[1] == -1:
            solve = a
            break

        for i in range(8):
            temp = a + binary_converter(i)
            b = i ^ 1
            c = decimal_converter(temp[len(temp)-b-3: len(temp)-b])
            b = b ^ c
            b = b ^ 4
            if b % 8 == goal:
                solutions.insert(0, (a + binary_converter(i), top[1]-1))
print(solve)
ans = 0
power = 1
for i in range(len(solve)):
    digit = int(solve[len(solve)-i-1])
    ans = ans + digit * power
    power = power * 2
print(ans)
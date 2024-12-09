import copy
f = open("data.txt", "r")

data = []
for line in f:
    parity = 0
    id = 0
    for char in line:
        if parity == 0:
            for i in range(int(char)):
                data.append(id)
            id = id + 1
        else:
            for i in range(int(char)):
                data.append(-1)
        parity = (parity + 1)%2

leftpointer = 0
rightpointer = len(data)-1

data_1 = copy.deepcopy(data)
data_2 = copy.deepcopy(data)
while rightpointer > leftpointer:
    while(data_1[rightpointer] == -1):
        rightpointer = rightpointer - 1
    while(data_1[leftpointer] != -1):
        leftpointer = leftpointer + 1
    if leftpointer >= rightpointer:
        break
    rightdata = data_1[rightpointer]
    data_1[leftpointer] = rightdata
    data_1[rightpointer] = -1
    rightpointer = rightpointer - 1
    leftpointer = leftpointer + 1

rightpointer = len(data) - 1
while rightpointer > 0:
    while data_2[rightpointer] == -1: # gets to chunk of memory
        rightpointer = rightpointer -1
    data_block = [0,0]
    data_block[1] = rightpointer + 1
    rightval = data_2[rightpointer]
    while data_2[rightpointer] == rightval:
        rightpointer = rightpointer - 1
    if rightpointer <= 0:
        break
    data_block[0] = rightpointer + 1
    leftpointer = 0
    while leftpointer < rightpointer:
        while data_2[leftpointer] != -1:
            leftpointer = leftpointer + 1
        memory_block_start = leftpointer
        if leftpointer >= rightpointer:
            break
        while data_2[leftpointer] == -1:
            leftpointer = leftpointer + 1
        if (leftpointer - memory_block_start) >= data_block[1] - data_block[0]:
            for i in range((data_block[1] - data_block[0])):
                data_2[(i + memory_block_start)] = data_2[(i + data_block[0])]
                data_2[(i + data_block[0])] = -1
            #print("memory block fits!")
            break
        
        


checksum = 0

new_checksum = 0
for index, value in enumerate(data_1):
    if value != -1:
        checksum = checksum + index*value

for index, value in enumerate(data_2):
    if value != -1:
        new_checksum = new_checksum + index*value
print(f"resulting checksum = {checksum}")
print(f"resulting checksum with new method = {new_checksum}")
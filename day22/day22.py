
def mix_prune(num1, num2):
    mixed = num1 ^ num2
    return mixed % 16777216

def step(num):
    result = num
    result = mix_prune(result, result * 64)
    result = mix_prune(result, int(result/32))
    result = mix_prune(result, result * 2048)
    return result

def get_front(num):
    num = str(num)
    return int(num[0])

def id(num1, num2, num3, num4):
    return 19**3 * (num1 + 9) + 19**2 * (num2 + 9) + 19 * (num3 + 9) + (num4 + 9)

sum = 0
f = open("data.txt", "r")

data = [] # treat -1 as 0 for future computations


for line in f:
    line_data = 19**4 * [-1]

    num = int(line)

    prev1 = num % 10
    num = step(num)
    prev2 = num % 10
    num = step(num)
    prev3 = num % 10
    num = step(num)
    prev4 = num % 10

    for i in range(1997):
        num = step(num)
        num_id = id(num%10-prev4, prev4-prev3, prev3-prev2,prev2-prev1)
        prev1 = prev2
        prev2 = prev3
        prev3 = prev4
        prev4 = num%10
        if line_data[num_id] == -1:
            line_data[num_id] = num%10
    sum = sum + num
    data.append(line_data)

max_price = 0
for i in range(len(data[0])):
    price = 0
    for z in range(len(data)):
        if data[z][i] != -1:
            price = price + data[z][i]
    max_price = max(max_price, price)
print(sum)
print(max_price)
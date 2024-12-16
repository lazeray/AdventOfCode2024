import numpy.linalg as la
import numpy as np
f = open("data.txt", "r")
lines = f.readlines()
index = 0 


sumscores = 0
while index < len(lines):
    a_line = lines[index]
    b_line = lines[index+1]
    prize_line = lines[index+2]
    index = index + 4
    a_data = a_line.split()
    b_data = b_line.split()
    prize_data = prize_line.split()
    a = [int(a_data[2][2:len(a_data[2])-1]), int(a_data[3][2:len(a_data[3])])]
    b = [int(b_data[2][2:len(b_data[2])-1]), int(b_data[3][2:len(b_data[3])])]
    prize = [int(prize_data[1][2:len(prize_data[1])-1]), int(prize_data[2][2:len(prize_data[2])])]
    prize[0] = prize[0] + 10000000000000
    prize[1] = prize[1] + 10000000000000
    #case1: a, b are in a line
    if np.isclose((b[0]/a[0]), (b[1]/a[1])):
        print("inline")
        if prize[0]/a[0] == prize[1]/a[1]: # prize is in the same line, there is possibly a solve
            if a[0]/b[0] > 3: # more value to use A
                for i in range(101):
                    target = prize[0] - b[0]*i
                    if target % a[0] == 0: # success!
                        sumscores = sumscores + i + 3 * target / a[0]
                        break
            else: # more value to use B 
                for i in range(101):
                    target = prize[0] - a[0]*i
                    if target % b[0] == 0: # success!
                        sumscores = sumscores + 3 * i + 3 * target / b[0]
                        break
            # do stuff
    else: # there is only 1 solution, or zero
        # doing a little cheating, since i'm lazy!
        temp_a = b[0]*a[1]
        temp_b = b[1]*a[0]
        target = prize[1]*a[0] - prize[0]*a[1]
        y_coeff = temp_b - temp_a
        if target % y_coeff == 0:
            y = int(target / y_coeff)
            if (prize[0] - b[0]*y) % a[0] == 0:
                x = int((prize[0] - b[0]*y) / a[0])
                sumscores = sumscores + 3*x + y
        

    

    

print(f"fewest tokens needed = {int(sumscores)}")

f.close()
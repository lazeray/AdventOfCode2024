import time
f = open("data.txt", "r")

x = 101
y = 103

finalmap = {}

def printstatus(finalmap):
    for i in range(x):
        for z in range(y):
            if (i, z) in finalmap:
                print(finalmap[(i,z)], end="")
            else:
                print(".", end="")
        print("")
    time.sleep(0.25)

for i in range(10000):
    f.seek(0)
    finalmap = {}
    for line in f:
        data = line.split()
        p = data[0].split(",")
        p_x = int(p[0].split("=")[1])
        p_y = int(p[1])
        v = data[1].split(",")
        v_x = int(v[0].split("=")[1])
        v_y = int(v[1])
        
        end_x = (p_x + i * v_x) % x
        end_y = (p_y + i * v_y) % y
        if (end_x, end_y) in finalmap:
            finalmap[end_x, end_y] = finalmap[end_x, end_y] + 1
        else:
            finalmap[end_x, end_y] = 1
    quadrants = [0,0,0,0]
    for location in finalmap:
        left = False
        right = False
        top = False
        bottom = False
        if location[0] < int(x/2):
            left = True

        if x % 2 != 0:
            if location[0] > int(x/2):
                right = True
        else:
            right = True    
        
        if location[1] < int(y/2):
            bottom = True
        if y % 2 != 0 :
            if location[1] > int(y/2):
                top = True
        else:
            top = True

        if right and top:
            quadrants[0] = quadrants[0] + finalmap[location] 
        if right and bottom:
            quadrants[1] = quadrants[1] + finalmap[location] 
        if left and top:
            quadrants[2] = quadrants[2] + finalmap[location]
        if left and bottom:
            quadrants[3] = quadrants[3] + finalmap[location]
    safety_factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    if safety_factor < 70000000:
        print(i)
        printstatus(finalmap)
        
        

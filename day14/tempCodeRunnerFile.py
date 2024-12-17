
        else:
            finalmap[end_x, end_y] = 1
    closeness = 0
    floodx = [-1,-1,-1,0,0,1,1,1]
    floody = [-1,0,1,-1,1,-1,0,1]
    for el in finalmap:
        for z in range(8):
            if (el[0] + floodx[z], el[1] + floody[z]) in finalmap:
                closeness = closeness + 1
    if closeness > 350:
        print(closeness)
        print(i)
        printstatus(finalmap)
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
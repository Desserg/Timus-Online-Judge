xyc = list(map(int, input().split(' ')))

if xyc[2] == 0:
        print(0, 0)
elif xyc[0]  >= xyc[2]:
    print(xyc[2], 0)    
elif xyc[1] >= xyc[2]:
    print(0, xyc[2])
elif xyc[0] + xyc[1] >= xyc[2]:
    if xyc[0] >= xyc[1]:
        print(xyc[2] - xyc[1], xyc[1])
    else:
        print(xyc[0], xyc[2] - xyc[0])
else:
    print("Impossible")
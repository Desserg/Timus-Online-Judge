'''
def P(x, y):
    if (x>0) and (y>0):
        for i in range(1, x+y+1):
            y = x*x+y
            x = x*x+y
            y = round((x+(y/abs(y))*(-abs(y)))**0.5)
            for j in range(1, 2*y+1):
                x = x-y
    print(x, y)
    return x, y
'''
xy = list(map(int, input().split()))
x = xy[0]
y = xy[1]
if x == y or x < 0 or 0 > y:
    print(x, y)
elif (x%2 == 0 and y%2 == 0) or (x%2 != 0 and y%2 != 0):
    print(x, y)
else:
    print(y, x)
    


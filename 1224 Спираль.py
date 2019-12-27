xy = list(map(int, input().split(' ')))

if xy[0] <= xy[1]:
    print(2*xy[0] - 2)
else:
    print(2*xy[1] - 1)


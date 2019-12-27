import sys

nS = list(map(int, input().split(' ')))
for x in sys.stdin:
    koord = list(map(int, x.rstrip().split(' ')))
koord = sorted(koord)
#print(koord)
if nS[1] == 0:
    print(0, 0)
elif koord[-1] < 0 < nS[1]:
    print(nS[1], nS[1]-koord[-1] + 0-koord[-1])
elif nS[1] < 0 < koord[0]:
    print(koord[0]-nS[1] + koord[0], 0 - nS[1])
elif nS[0] == 1:
    print('Impossible')
else:
    error = True
    x = 0
    while nS[1] > koord[x]:
        error = False
        x += 1
        if x == nS[0]:
            error = True
            break
    if error:
        print('Impossible')
    else:
        a = koord[x-1]
        b = koord[x]
        #print(a, b)     
        if (nS[1] < 0 and b < 0) or (nS[1] > 0 and a > 0): 
            print('Impossible')
        else:
            if nS[1] > 0:
                print(nS[1], (0 - a) + (nS[1]-a))
            else:
                print(b + b-nS[1], 0-nS[1])

import sys
nts = list(map(int, input().split()))

gondols = []
for x in sys.stdin:
    gondols = list(map(int, x.rstrip().split(' ')))
    
T = nts[1] + nts[2]
for i in range(nts[0]):
    temp = T - (T-gondols[i])/2
    print('%0.6f' % temp)


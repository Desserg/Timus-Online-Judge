n = int(input())
stek = sum(list(map(int , input().split(' '))))

if (stek - n)/2 % 2 == 0:
    print('Stannis')
else:
    print('Daenerys')
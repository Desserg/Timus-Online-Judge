nk = list(map(int, input().split(' ')))
droid = nk[1]
bumbum = list(map(int, input().split(' ')))
balance_bum = 0
balance_droid = 0
for n in range(nk[0]):
    if bumbum[n] > droid:
        balance_bum += bumbum[n] - droid
    else:
        balance_droid += droid - bumbum[n]
print(balance_bum, balance_droid)        

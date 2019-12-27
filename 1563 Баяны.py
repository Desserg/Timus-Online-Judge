market = list(input() for _ in range(int(input())))

bajan = 0
vizit = []

for i in market:
    if i in vizit:
        bajan +=1
    else:
        vizit.append(i)
        
print(bajan)
    
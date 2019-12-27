banknots = list(map(int, input().split()))
cost = int(input())
val = [10, 50, 100, 500, 1000, 5000]

summ = 0
for i in range(6):
    summ += banknots[i]*val[i]
    
for id, item in enumerate(banknots):
    if item > 0:
        m_banknot = val[id]
        break

min_cost = cost*((summ - m_banknot) // cost + 1)
ostatok = summ - min_cost
x = ostatok // cost
if ostatok == 0:
    print(1)
    print(min_cost//cost)
else:
    print(x+1)
    for i in range(x+1):
        print(min_cost//cost + i, end=(' '))
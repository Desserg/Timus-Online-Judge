n = int(input())
k = int(input())

#https://acm.timus.ru/forum/thread.aspx?id=11567&upd=632567801246562500
# объяснил почему так
TrueN = []
TrueN.append(k-1)
TrueN.append(k*TrueN[0])

for i in range(2, n):
    TrueN.append((k-1)*(TrueN[i-1] + TrueN[i-2]))
print(TrueN[n-1])

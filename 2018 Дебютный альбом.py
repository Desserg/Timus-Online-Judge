#не работает неправильный подход

nab =  list(map(int, input().split()))

a = min(nab[1], nab[2])
b = max(nab[1], nab[2])

def trek(i):
    if i == 0:
        return 1
    elif 0 < i <=a:
        return 2**i
    elif a < i <= b:
        return 2*trek(i-1) - 1
    
if nab[0] <= b:
    con = trek(nab[0])
    print(con % (10**9 + 7))
else:
    con = trek(b)
    k = nab[0] - b
    print((2**k * con - 2*(2**k-1)) % (10**9 + 7))
    



n = int(input())
a = int(input())

def zeroM(n):
    m = []
    for i in range(n):
        m.append(0)
    return m


def stateL(m):
    
        
    
'''
def zero(n, k):
    st = bin(n)[2:].zfill(k)
    z = 0
    for i in st[::-1]:
        if i == '0':
            z += 1
        else: break
    return z

def zeroM(n):
    m = []
    for i in range(n):
        m.append(0)
    return m

def zeroA(e):
    m = []
    for i in range(e, 0, -1):
        m.append(2**(i-1))
    m.append(1)
    return m
"""
for y in range(n-a+1):
    m = zeroM()
    for x in range(2**(a+y)):
        m[zero(x, n)] += 1 
    print(m)
"""    
'''


    

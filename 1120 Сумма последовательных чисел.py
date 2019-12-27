n = int(input())

'''
# x = (-(2*A - 1) + sqrt((2*A-1)**2 + 8*N))/2
def brute_forceA(A, N):
    return (-(2*A - 1) + ((2*A-1)**2 + 8*N)**.5)/2
'''

def brute_forceP(P, N):
    return N/P - (P-1)/2


pp = int((1 + (1 + 8*n)**.5)/2) # p не может быть больше этой границы
#aa = 1
while pp >= 1:
    a = brute_forceP(pp, n)
#    p = brute_forceA(aa, n)
    if (a * 10) % 10 == 0 and a > 0:
        break
#    if (p * 10) % 10 == 0:
#        break
    else:
        pp -= 1
#        aa += 1
        
#p = int(p)
a = int(a)

#print(aa, p)
print(a, pp)






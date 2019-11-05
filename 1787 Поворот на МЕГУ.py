kn = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))
'''
"Неверно!
например тест
4 3
3 4 5"
SumA = sum(A)
Probka = SumA - int(nk[0])*int(nk[1])

if Probka <= 0:
    print(0)
else:
    print(Probka)
'''
ij = 0
for i in A:
    Pi = (i - kn[0]) + ij
    if Pi <= 0:
        Pi = 0
    ij = Pi
print(Pi)
from fractions import Fraction

NM = list(map(int, input().split(' ')))

NM = sorted(NM)

m = NM[0] - 1
n = NM[1] - 1

a = Fraction(m, n)
k = int(m/a.numerator)
if n%m == 0:
    print(n)
elif int(m/a.numerator) == m:
    print(k)
    print(n + m - 1)
else:
    print(int(k*(m/k + n/k -1)))

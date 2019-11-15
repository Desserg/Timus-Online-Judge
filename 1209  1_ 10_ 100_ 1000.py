st = []
N = int(input())
# третий вариант через дескреминант (не хотел но пришлось)
'''
So let's try to check whether an input A is a position of '1'.
N*(N-1)/2 + 1 = A;
N^2 - N + 2 - 2*A = 0;
N is natural, so solution is:
N = 1/2 * (1 + sqrt(8*A - 7));
So, A is a position if sqrt(8*A-7) is natural.
'''
for i in range(N):
    n = int(input())
    if float.is_integer((8*n-7)**0.5):
        st.append(1)
    else:
        st.append(0)
for i in st:
    print(i, end = ' ')
        
''' правильный алгорим но долгий >1 секунды по тестам
for i in range(N):
    n = int(input())
    arpr = 0
    while n > 0:
        n -= arpr
        arpr += 1 # степень основания 10
    l = list(range(arpr-1))
    if l[n-1] == 0:
        st.append(1)
    else:
        st.append(0)
for i in st:
    print(i, end = ' ')
'''
# после некоторых размышлений - свойство арифметической прогрессии
# сумма = (n+1)n/2

# тоже не проходит по времени (вычисляем позиции всех "1")
'''
All = []
i = 0
s = 0
st = []
while s < (2**31 -1):
    s = (i+1)*i/2 +1
    All.append(s)
    i += 1
for i in range(N):
    n = int(input())
    if n in All:
        st.append(1)
    else:
        st.append(0)
for i in st:
    print(i, end = ' ')        '''
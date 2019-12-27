from itertools import count # izip for maximum efficiency
import time
from collections import Counter

#Разложить число на множители
def get_ls(n):
    #result = [1]
    result = []
    i = 2
    while i < n:
        if n % i == 0:
            n /= i
            result.append(i)
        else:
            i += 1
    result.append(int(n))
    return result
 
def Triviality(N):
    ls = get_ls(N)
    kkk = dict(Counter(ls)).items()
    d = [k for k, _ in kkk]
    m = [v for _, v in kkk]
    k = [0 for _ in range(len(set(ls)))]
    ln = range(len(m))
    try:
        sum_r = 0
        while True:
            r = 1
            for i1, i2 in zip(d, k):
                r *= i1 ** i2
            sum_r += r
            k[0] += 1
            for i in ln:
                if k[i] > m[i]:
                    k[i] = 0
                    k[i+1] += 1  # IndexError
    except IndexError:
        pass
    return (sum_r-N)/N

#поиск всех простых на N
def sieve(n):
    S = []
    S.append(0) # 0 - не простое число
    S.append(0) # 1 - не простое число
    # заполняем решето единицами
    S += [1] * (n-1)
    for k in range(2, int((n+1)**0.5 + 1)):
        # если k - простое (не вычеркнуто)
        if (S[k] == 1): 
            #то вычеркнем кратные k
            for l in range(k*k, n+1, k):
                S[l] = 0
    return S

def f(n1, n2):
    simple = sieve(n2)
    slice_search = simple[n1:]
    index_simple = [i for i, j in zip(count(), simple) if j == 1]
    if index_simple[-1] > n1:
        # есть простые, значит самое большое из них искомое
        return index_simple[-1]
    else:
        for j in range(n2-n1 + 1):
            slice_search[j] = Triviality(j+n1)
    return slice_search.index(min(slice_search)) + n1

n1, n2 = map(int, input().split())
if n1 == 1: print(1) #еденица - сама тревиальность = 0 
elif n1==n2: print(n1)
else:
    #start_time = time.time()
    print(f(n1, n2))
    #print("--- %s seconds ---" % (time.time() - start_time))  

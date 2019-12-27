from collections import Counter

def get_ls(n):
    """Разложить число на множители"""
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

print(Triviality(10))
    
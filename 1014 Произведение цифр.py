n = int(input())
def search(k):
    k_list = []
    for j in range(9, 1, -1):
        k, r = numb(k, j)
        if r != 0: temp = [j]*r
        else: temp = []
        k_list += temp
    if k == 1: return k_list
    else: return []
def numb(n, el):
    k = 0
    while n >= el:
        if n % el == 0:
            n = n//el
            k += 1
        else: break
    return n, k
if n == 0:
    print(10)
elif 9 >= n >= 1:
    print(n)
elif n >= 10:
    sort_list = search(n)
    if sort_list == []:
        print(-1)
    else:
        for i in sort_list[::-1]:
            print(i, end='')
        

    

N = int(input())
e = m = l = 0
for i in range(N):
    str = input()
    if 'E' in str:
        e += 1
    if 'M' in str:
        m += 1
    if 'L' in str:
        l += 1
if e > m and e > l:
    print('Emperor Penguin')
if m > e and m > l:
    print('Macaroni Penguin')
if l > e and l > m:
    print('Little Penguin')

NUMB = int(input())

NUMB1 = NUMB + 1
NUMB_1 = NUMB - 1

def prb(x):
    result = []
    while x > 0:
        result.append(x % 10)
        x //= 10

    result.reverse()
    return(result)

A1 = sum(prb(NUMB1//1000))
B1 = sum(prb(NUMB1%1000))
A_1 = sum(prb(NUMB_1//1000))
B_1 = sum(prb(NUMB_1%1000))

if A1 == B1 or A_1 == B_1:
    print('Yes')
else:
    print('No')



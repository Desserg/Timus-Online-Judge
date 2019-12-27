import sys

n = int(input())
def guzzle(i):
    if i == 0:
        return stripies[0]
    if i == 1:
        return 2*(stripies[i]*stripies[i-1])**.5
    else:
        return 2*(stripies[i]*guzzle(i-1))**.5

stripies = []

for x in sys.stdin:
    stripies.append(int(x.strip()))

stripies = sorted(stripies, reverse = True)

print('%.2f' % guzzle(n-1))
import sys
n, s = map(int, input().split())
out = []
temp = s
for x in sys.stdin:
    number = int(x.rstrip())
    out.append(temp//number - 1)
    temp = number
out = ' '.join([str(i) for i in out])
sys.stdout.write(out)
sys.stdout.flush()

import sys

for line in sys.stdin:
    print(line.rstrip('\n')[::-1])
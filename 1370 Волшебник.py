import sys
nm = list(map(int, input().split(' ')))
number_ring = list(map(str.rstrip, sys.stdin))

element_num1 = nm[1] % nm[0]
if nm[0] - element_num1 - 10 >= 0:
    for x in range(element_num1, element_num1 + 10):
        print(number_ring[x], end='')
else:
    for x in range(element_num1, nm[0]):
        print(number_ring[x], end='')
    for x in range(abs(nm[0] - element_num1 - 10)):
        print(number_ring[x], end='')
    
    
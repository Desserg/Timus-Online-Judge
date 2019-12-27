import fileinput
import sys


np = list(map(int, input().split(' ')))

for line in fileinput.input():   # читает строку после строки, пока нет Ctrl+D
    lst = line.split()           # lst будет списком отдельных чисел, но как строк

n = np[0]
p = np[1]


print(n*(n-1)//2 - p)
import sys

def input_hat():
    facultys = ('Slytherin', 'Hufflepuff', 'Gryffindor', 'Ravenclaw')
    n = int(input())
    persons = list(map(str.rstrip, sys.stdin))
    for fac in facultys:
        print(fac + ':')
        for i in range(n):
            if persons[2*i + 1] == fac:
                print(persons[2*i])
        if fac != facultys[3]:
            print()
    return

input_hat()



import sys
facultys = ('Slytherin', 'Hufflepuff', 'Gryffindor', 'Ravenclaw')

def input_hat():
    n = int(input())
    person = [[],[],[],[]]

    name = ''
    for i in map(str.rstrip, sys.stdin):
        if i not in facultys:
            name = i
        else:
           person[facultys.index(i)].append(name)    
    return person

def output_hat(person):
    x = 0
    for fac in facultys:
        print(fac + ':')
        for name in person[x]:
            print(name)
        x += 1
        if x < 4:
            print()
    return
    
output_hat(input_hat())

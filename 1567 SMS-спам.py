stroka = list(input())
c = {1: 'adgjmpsvy. ', 2: 'behknqtwz,', 3: 'cfilorux!'}

n = 0
for i in stroka:
    for name, cont in c.items():
        if  cont.find(i) != -1:
            n += name
print(n)
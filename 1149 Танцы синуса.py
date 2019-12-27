n = int(input())

x = 0
z = n
def An(i):
    if i == 1:
        return 'sin('+ itsin() + ')'
    else:
        return('sin(' + itsin() + znak() + str(An(i-1)) + ')')
    
def itsin():
    global x
    x += 1
    return str(x)

def  znak():
    global x
    if x%2 == 0:
        return '+'
    else:
        return '-'
    
strsn = ''
for skoba in range(1, n):
    strsn += '('
for z in range(1, n+1):
    x = 0
    strsn += An(z) + '+' + str(n+1-z) + ')'

print(strsn[0:-1])
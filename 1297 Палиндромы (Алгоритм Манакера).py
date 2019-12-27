string = input()

#Наивный алгоритм
'''
n = len(string)
string2 = '!#'

t = [] # в этом списке будем хранить расстояния от центра до границы палиндрома
for i in range(n):
    t.append(0)
    t.append(0)
    string2 += string[i] + '#'
string = string2 + '$'    
n = len(string)

for i in range(2, n - 3):
    while (string[i - t[i - 1]] == string[i + t[i - 1]]):
        t[i - 1] += 1

lpal = max(t)
center = t.index(lpal) + 1
fin_string = string[(center - lpal + 2): (center + lpal - 1)]
print(fin_string) # необходимо удалить "#"
'''    
    
def manacher_odd(s):
    n = len(s)
    d = []
    for i in range(n):
        d.append(1)
    l = 0
    r = 0
    for i in range(1, n):
        if i < r:
            d[i] = min(r - i + 1, d[l + r - i])
        while (i - d[i] >= 0 and i + d[i] < n and s[i - d[i]] == s[i + d[i]]):
            d[i] += 1
        if (i + d[i] - 1 > r):
            l = i - d[i] + 1
            r = i + d[i] - 1
    return d

string2 = '#'
for i in range(len(string)):
    string2 += string[i] + "#"

Palindroms = manacher_odd(string2)

lpal = max(Palindroms)
center = Palindroms.index(lpal)
temp = 0
if lpal == 2 and len(string) > 2:
    fin_string = string[0]
else:
    string2 = string2[(center - lpal + 1): (center + lpal)]
    fin_string = ''
    for i in range(len(string2)):
        if string2[i] != '#':
            fin_string += string2[i] 
        
print(fin_string)


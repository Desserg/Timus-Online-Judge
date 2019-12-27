
# Вариант 3 (идея проверять i-ый символ на равенство с i-1) работает

def foo(stroka):
    f = 0
    newst = ''
    ln = len(stroka)
    for i in range(1, ln):
        if stroka[i] != stroka[i-1] and f == 0:
            newst += stroka[i-1]
        elif  stroka[i] == stroka[i-1] and f != 1:
            f = 1
        elif f == 1 and newst == '':
            f = 0
        elif f == 1 and stroka[i] == newst[-1]:
            newst = newst[:-1]
        elif f == 1 and (stroka[i] != newst[-1]):
            f = 0
    if f == 0:
        newst += stroka[-1]
    return newst

shifr = input()
st = foo(shifr)
print(st)

'''
# Вариант 2 (№6 TLE)
def foo(stroka):
    i = 0
    while (i <= len(stroka) - 2) and (len(stroka) > 1):
        if stroka[i] == stroka[i+1]:
            stroka.pop(i+1)
            stroka.pop(i)
            i += 1
        else:
            i += 1
    return stroka

shifr = list(input())
shifr.append('!')

f = True
while f:
    len1 = len(shifr)
    st = foo(shifr)
    len2 = len(st)
    if (len1 == len2) or (st[0] == '!'):
        f = False
print(''.join(st[0:-1]))
'''

'''
# вариант 1 (7 тест TLE)
import re
def foo(strok):
    f = True
    while f:
        shifr1 = strok
        strok = re.sub(r'(\w)\1', '', strok)
        if shifr1 == strok:
           f = False 
    return strok
print(foo(shifr))    
'''


import time
start_time = time.time()

import sys
sys.setrecursionlimit(4001)

n= int(input())
mandat = []
for x in sys.stdin:
    mandat.append(int(x.strip()))
    
MyDict = {}
v = mandat[-1]
result = []
def buildP(mandat):
    current = mandat.pop()
    if len(mandat) == 0:
        return
    else:
        if mandat[-1] > current:
            idmax = len(mandat)
        else:
            idmax = -1
        idmin = -1
        for id, item in enumerate(mandat[::-1]):
            if item < current:
                idmin = len(mandat) - id
                break
        MyDict[current] = [mandat[idmin - 1] if idmin != -1 else None, mandat[idmax - 1] if idmax != -1 else None]
        if idmin > 0:
            buildP(mandat[0: idmin])
        if idmax > 0:
            if idmin == -1: idmin = 0
            buildP(mandat[idmin: idmax])
def sbor(root):
    if MyDict.get(root, -1) == -1:
        return root
    else:
        if MyDict[root][1] != None:
            result.append(sbor(MyDict[root][1]))
        if MyDict[root][0] != None:
            result.append(sbor(MyDict[root][0]))
        return result.append(root)
    
if len(mandat) == 1:
    print(mandat[0])
else:
    buildP(mandat)
    sbor(v)
    for i in result:
        if i != None:
            print(i)
print("--- %s seconds ---" % (time.time() - start_time))
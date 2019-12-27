import sys
spis = []
for x in sys.stdin:
    spis.append(x.strip())
dev = {}
for i in range(6):
    if dev.get(spis[1+3*i]) == None:
        dev[spis[1+3*i]] = [(-1), int(spis[2+i*3])]
    else:
        dev[spis[1+3*i]][0] -= 1
        if dev[spis[1+3*i]][1] > int(spis[2+i*3]):
            dev[spis[1+3*i]][1] = int(spis[2+i*3])
list_dev = list(dev.items())
dev_sort = sorted(list_dev, key=lambda k: (k[1][0], k[1][1]))
print(dev_sort[0][0])
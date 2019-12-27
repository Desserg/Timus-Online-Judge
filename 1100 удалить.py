a=[]
for i in range(int(input())):
    c=str(input())
    if len(a)==0 :
        a.append(c)
        continue
    d=(a[0].split())[1]
    d=int(d)
    k=int((c.split())[1])

    if k>=d :
        a.reverse()
        a.append(c)
        a.reverse()
    else:
        for j in range (len(a)):
            h=int((a[j].split())[1])

            if k >= h:
                p = a[:j]
                o = a[j:]
                p.append(c)
                p.extend(o)

for i in range(len(a)):
   print(a[i])

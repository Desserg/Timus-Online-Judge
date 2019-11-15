nm = list(map(int, input().split(' ')))
urna = []
for i in range(nm[0]):
    urna.append(0)
for i in range(nm[1]):
    urna[int(input())-1] += 1
P100 = sum(urna)
for i in range(nm[0]):
    A = urna[i]/P100*100
    print("%.2f" %A, end = "%\n")
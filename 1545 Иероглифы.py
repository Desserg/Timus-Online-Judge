n = int(input())

dic = []
rep = []

for i in range(n):
    dic.append(input())
hieroglyph = input()

for i in range(n):
    if dic[i].startswith(hieroglyph):
        rep.append(dic[i])
if len(rep) == 0:
    exit
else:
    for i in range(len(rep)):
        print(rep[i])



import sys
n = int(input())
dignity = {}
for x in sys.stdin:
    tempkey = x.strip()
    if dignity.get(tempkey) == None:
        temp = 1
    else:
        temp = dignity.get(tempkey) + 1
    dignity.update({tempkey: temp})
        
final_dict = list([max(dignity.items(), key=lambda k_v: k_v[1])])

print(final_dict[0][0])



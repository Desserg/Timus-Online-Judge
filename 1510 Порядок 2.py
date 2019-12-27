import sys

def method():
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
    return final_dict[0][0]

print(method())
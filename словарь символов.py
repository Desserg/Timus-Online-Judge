import string

di = dict(zip(string.ascii_uppercase,[(ord(c)%32 + 9) for c in string.ascii_uppercase]))
print(di)
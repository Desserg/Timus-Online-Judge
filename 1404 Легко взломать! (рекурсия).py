import string

abc_ = string.ascii_lowercase
st_in = input()
st_out = ''

def deshifr(i):
    global st_out
    if i == 0:
        st_index = (abc_.find(st_in[0]) - 5 + 26) % 26
        st_out += abc_[st_index]
        return st_index + 5
    else:
        temp = deshifr(i-1)
        st_index = (abc_.find(st_in[i]) - temp + 26) % 26
        st_out += abc_[st_index]
        return st_index + temp 
 
deshifr(len(st_in) - 1)
print(st_out)
              

import string

abc_ = string.ascii_lowercase
st = input()
st_final = ''

current_index = 0
for i in range(len(st)):
    if i == 0:
        current_index = (abc_.find(st[i]) + 26) % 26
        st_final += abc_[current_index - 5]
    else:
        next_index = (abc_.find(st[i]) + 26) % 26
        st_final += abc_[(abc_.find(st[i]) - current_index + 26) % 26]
        current_index = next_index
        
print(st_final)
st = []
N = int(input())
All = []
i = 0
s = 0
while s < (2**31 -1):
    s = (i+1)*i/2 +1
    All.append(s)
    i += 1
for i in range(N):
    n = int(input())
    if n in All:
        st.append(1)
    else:
        st.append(0)
for i in st:
    print(i, end = ' ')   
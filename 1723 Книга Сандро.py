from collections import Counter


s = input()
c = Counter(s)

a = c.most_common(1)
print(*a[0][0])

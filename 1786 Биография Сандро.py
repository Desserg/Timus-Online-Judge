def distance(a, b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    current_row = range(n + 1)  # Keep current and previous row, not entire matrix
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            change = previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = change

    return current_row[n]

def level(string):
    string1 = string[:]
    string1 = string1.capitalize()
    a = distance(string1, string)
    return a

st = input()
metric = []
for i in range(len(st)-6 + 1):
    sub_st = st[i: i+6]
    reg = level(sub_st) * 5
    sub_st = sub_st.capitalize()
    metric.append(distance('Sandro', sub_st) * 5 + reg)
print(min(metric))



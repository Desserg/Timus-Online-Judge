import sys, re

ptrn = r'[!?.]\s*-*\s*\w+'
text = ''

def title_sumbol(m):
    st = m.group(0)
    return st.title()

def Up_sumbol(m):
    st = m.group(0)
    st2 = st[0] + st[1:].title()
    return st2

for line in sys.stdin:
    text += str(line)

text = text.lower()
text2 = re.sub(r'\w', title_sumbol, text, 1)
text3 = re.sub(ptrn, Up_sumbol, text2)
print(text3)


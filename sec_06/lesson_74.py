s = "aaaceafeagpceamgteage"

print('# dictを使用')
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

print('# dictのsetdefaultを使用')
d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

print('# collections.defaultdictを使用')
from collections import defaultdict
d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)

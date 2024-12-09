aa = [l for l in open("./2024/input9.txt")]
a = aa[0]
f = []
c = 0
t = False
s = []
for i in range(len(a)):
  if a[i] == '\n':
    break
  n = int(a[i])
  for j in range(0, n):
    if not t:
      f.append(c)
    else:
      f.append('.')
      s.append(len(f) - 1)
  if not t:
    c += 1
  t = not t
k = 0
ski = 0
c -= 1
i = len(f) - 1
while i > 0:
  if f[i] == c:
    start = i
    jj = 0
    while f[i] == c:
      jj += 1
      i -= 1
    i += 1
    c -= 1
    end = i
    m = 0
    jjj = 0
    startd = 0
    endd = 0
    y = True
    while m < end:
      if y and f[m] == '.':
        startd = m
        y = False
      if f[m] == '.':
        jjj += 1
      else:
        y = True
        jjj = 0
      if jjj == jj:
        endd = m
        break
      m += 1
    if m == end:
      i -= 1
      continue
    mmm = end
    o = c + 1
    for mm in range(end, start + 1):
      f[startd] = o
      startd += 1
      f[mmm] = '.'
      mmm += 1
  i -= 1
su = 0
kk = 0
for i in range(len(f)):
  if f[i] == '.':
    kk += 1
    continue
  su += kk * f[i]
  kk += 1
print(su)
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
for i in range(len(f) - 1, -1, -1):
  if k >= len(s) - ski:
    break
  if f[i] != '.':
    f[s[k]] = f[i]
    f[i] = '.'
    k += 1
  else:
    ski += 1
su = 0
kk = 0
for i in range(len(f)):
  if f[i] == '.':
    break
  su += kk * f[i]
  kk += 1
print(su)
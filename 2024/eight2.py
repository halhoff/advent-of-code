a = [l.strip() for l in open("./2024/input8.txt")]
l = {}
for j in range(len(a)):
  for i in range(len(a[0])):
    m = a[j]
    q = a[j][i]
    if a[j][i] != '.':
      if a[j][i] not in l:
        l[a[j][i]] = [[j, i]]
      else:
        l[a[j][i]].append([j, i])
d = set()
for m in l.keys():
  p = l[m]
  for j in range(len(p)):
    d.add(tuple[p[j][0], p[j][1]])
  for j in range(len(p) - 1):
    for i in range(j + 1, len(p)):
      dx = p[j][0] - p[i][0]
      dy = p[j][1] - p[i][1]
      nx = p[j][0] + dx
      ny = p[j][1] + dy
      mx = p[i][0] - dx
      my = p[i][1] - dy
      while 0 <= nx < len(a[0]) and 0 <= ny < len(a):
        d.add(tuple[nx, ny])
        nx += dx
        ny += dy
      while 0 <= mx < len(a[0]) and 0 <= my < len(a):
        d.add(tuple[mx, my])
        mx -= dx
        my -= dy
print(len(d))

a = []
osx = -1
osy = -1
with open("./2024/input6.txt", 'r') as f:
  for l in f:
    a.append(l)
for i in range(len(a)):
  if '^' in a[i]:
    osx = a[i].index('^')
    osy = i
o = 0
for i in range(len(a)):
  for j in range(len(a[0])):
    if j < len(a[i]) and a[i][j] == '.':
      sx = osx
      sy = osy
      d = 'U'
      p = 0
      n = a[i][:j] + '#' + a[i][j + 1:]
      m = a[:i] + [n] + a[i + 1:]
      while 0 <= sx < len(m[0]) and 0 <= sy < len(m):
        if d == 'U':
          if m[sy - 1][sx] == '#':
            d = 'R'
            continue
          sy -= 1
          if not (0 <= sx < len(m[0]) - 1 and 0 <= sy < len(m) - 1):
            break
        elif d == 'D':
          if m[sy + 1][sx] == '#':
            d = 'L'
            continue
          sy += 1
          if not (0 <= sx < len(m[0]) - 1 and 0 <= sy < len(m) - 1):
            break
        elif d == 'L':
          if m[sy][sx - 1] == '#':
            d = 'U'
            continue
          sx -= 1
          if not (0 <= sx < len(m[0]) - 1 and 0 <= sy < len(m) - 1):
            break
        elif d == 'R':
          if m[sy][sx + 1] == '#':
            d = 'D'
            continue
          sx += 1
          if not (0 <= sx < len(m[0]) - 1 and 0 <= sy < len(m) - 1):
            break
        p += 1
        if p > 10000:
          o += 1
          break
print(o)
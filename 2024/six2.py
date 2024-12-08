a = [l.strip() for l in open("./2024/input6.txt")]
osx, osy = next((i, j) for j, l in enumerate(a) for i, c in enumerate(l) if c == '^')
o = 0
for i in range(len(a)):
  for j in range(len(a[0])):
    if j < len(a[i]) and a[i][j] == '.':
      sx, sy, d, p = osx, osy, 'U', 0
      m = a[:i] + [a[i][:j] + '#' + a[i][j + 1:]] + a[i + 1:]
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
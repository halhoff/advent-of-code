m = []
sx = -1
sy = -1
with open("./2024/input6.txt", 'r') as f:
  for l in f:
    m.append(l)
for i in range(len(m)):
  if '^' in m[i]:
    sx = m[i].index('^')
    sy = i
d = 'U'
p = [[sx, sy]]
while 0 <= sx < len(m[0]) and 0 <= sy < len(m):
  if d == 'U':
    sy -= 1
    if not (0 <= sx < len(m[0]) - 1 and 0 <= sy < len(m) - 1):
      break
    if m[sy - 1][sx] == '#':
      d = 'R'
  elif d == 'D':
    sy += 1
    if not (0 <= sx < len(m[0]) - 1 and 0 <= sy < len(m) - 1):
      break
    if m[sy + 1][sx] == '#':
      d = 'L'
  elif d == 'L':
    sx -= 1
    if not (0 <= sx < len(m[0]) - 1 and 0 <= sy < len(m) - 1):
      break
    if m[sy][sx - 1] == '#':
      d = 'U'
  elif d == 'R':
    sx += 1
    if not (0 <= sx < len(m[0]) - 1 and 0 <= sy < len(m) - 1):
      break
    if m[sy][sx + 1] == '#':
      d = 'D'
  if ([sx, sy]) not in p:
    p.append([sx, sy])
print(len(p))
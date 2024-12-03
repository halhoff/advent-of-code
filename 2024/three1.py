s = ""
sum = 0
with open("./2024/input3.txt", 'r') as f:
  for l in f:
    s += l
i = 0
e = True
while i < len(s):
  if s[i:i + 4] == "do()":
    e = True
  elif s[i:i + 7] == "don't()":
    e = False
  if e and s[i:i + 4] == "mul(":
    x = 0
    y = 0
    i += 4
    xx = i
    if i >= len(s):
      break
    while s[i].isdigit():
      i += 1
    x = int(s[xx:i])
    if s[i] != ',':
      i += 1
      continue
    else:
      i += 1
      yy = i
      while s[i].isdigit():
        i += 1
      y = int(s[yy:i])
      if s[i] != ')':
        i += 1
        continue
    sum += x * y
  i += 1
print(sum)
def isValidSymbol(x: str) -> bool:
  return x not in ".0123456789\n"
sum = 0
mat = []
with open("input3.txt", 'r') as file:
  for line in file:
    mat.append(line)
for index, line in enumerate(mat):
  i = 0
  line = line[:len(line) - 1]
  while i < len(line):
    if '0' <= line[i] <= '9':
      start = i
      while i < len(line) and '0' <= line[i] <= '9':
        i += 1
      end = i - 1
      if start > 0 and isValidSymbol(mat[index][start - 1]):
        sum += (int)(line[start:end + 1])
        continue
      elif end < len(line) - 1 and isValidSymbol(mat[index][end + 1]):
        sum += (int)(line[start:end + 1])
        continue
      if index != len(mat) - 1:
        if start > 0 and isValidSymbol(mat[index + 1][start - 1]):
          sum += (int)(line[start:end + 1])
          continue
        elif end < len(line) - 1 and isValidSymbol(mat[index + 1][end + 1]):
          sum += (int)(line[start:end + 1])
          continue
        toggle = False
        for j in range(start, end + 1):
          if isValidSymbol(mat[index + 1][j]):
            sum += (int)(line[start:end + 1])
            toggle = True
            break
        if toggle:
          continue
      if index != 0:
        if start > 0 and isValidSymbol(mat[index - 1][start - 1]):
          sum += (int)(line[start:end + 1])
          continue
        elif end < len(line) - 1 and isValidSymbol(mat[index - 1][end + 1]):
          sum += (int)(line[start:end + 1])
          continue
        toggle = False
        for j in range(start, end + 1):
          if isValidSymbol(mat[index - 1][j]):
            sum += (int)(line[start:end + 1])
            toggle = True
            break
        if toggle:
          continue
    i += 1
print(sum)
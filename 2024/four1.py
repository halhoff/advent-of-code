li = []
c = 0
with open("./2024/test.txt", 'r') as f:
  for l in f:
    li.append(l)
for j in range(len(li)):
  for i in range(len(li[j])):
    if li[j][i] == 'X':
      if i >= 3 and li[j][i - 3:i] == "SAM":
        c += 1
      if i <= len(li[j]) - 4 and li[j][i + 1:i + 4] == "MAS":
        c += 1
      if j >= 3 and li[j - 1][i] == 'M' and li[j - 2][i] == 'A' and li[j - 3][i] == 'S':
        c += 1
      if j <= len(li) - 4 and li[j + 1][i] == 'M' and li[j + 2][i] == 'A' and li[j + 3][i] == 'S':
        c += 1
      if i >= 3 and j >= 3 and li[j - 1][i - 1] == 'M' and li[j - 2][i - 2] == 'A' and li[j - 3][i - 3] == 'S':
        c += 1
      if i <= len(li[j]) - 4 and j >= 3 and li[j - 1][i + 1] == 'M' and li[j - 2][i + 2] == 'A' and li[j - 3][i + 3] == 'S':
        c += 1
      if i >= 3 and j <= len(li) - 4 and li[j + 1][i - 1] == 'M' and li[j + 2][i - 2] == 'A' and li[j + 3][i - 3] == 'S':
        c += 1
      if i <= len(li[j]) - 4 and j <= len(li) - 4 and li[j + 1][i + 1] == 'M' and li[j + 2][i + 2] == 'A' and li[j + 3][i + 3] == 'S':
        c += 1
print(c)
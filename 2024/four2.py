li = []
c = 0
with open("./2024/input4.txt", 'r') as f:
  for l in f:
    li.append(l)
for j in range(len(li)):
  for i in range(len(li[j])):
    if li[j][i] == 'A':
      if 1 <= i <= len(li[j]) - 2 and 1 <= j <= len(li) - 2 and li[j - 1][i - 1] == 'M' and li[j + 1][i - 1] == 'M' and li[j - 1][i + 1] == 'S' and li[j + 1][i + 1] == 'S':
        c += 1
      if 1 <= i <= len(li[j]) - 2 and 1 <= j <= len(li) - 2 and li[j - 1][i - 1] == 'S' and li[j + 1][i - 1] == 'S' and li[j - 1][i + 1] == 'M' and li[j + 1][i + 1] == 'M':
        c += 1
      if 1 <= i <= len(li[j]) - 2 and 1 <= j <= len(li) - 2 and li[j - 1][i - 1] == 'S' and li[j + 1][i - 1] == 'M' and li[j - 1][i + 1] == 'S' and li[j + 1][i + 1] == 'M':
        c += 1
      if 1 <= i <= len(li[j]) - 2 and 1 <= j <= len(li) - 2 and li[j - 1][i - 1] == 'M' and li[j + 1][i - 1] == 'S' and li[j - 1][i + 1] == 'M' and li[j + 1][i + 1] == 'S':
        c += 1
print(c)
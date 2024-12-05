l1 = []
l2 = []
sum = 0
with open("./2024/input5.txt", 'r') as f:
  for l in f:
    if l == '\n':
      continue
    if len(l) > 3 and l[2] == '|':
      l1.append(int(l[:2]))
      l2.append(int(l[3:5]))
    else:
      x = []
      n = 0
      for i in range(len(l)):
        if l[i] == '\n':
          continue
        if l[i] == ',':
          n = 0
        else:
          if n == 0:
            n = int(l[i])
          else:
            n *= 10
            n += int(l[i])
            x.append(n)
      bigsuc = True
      for i in range(len(x) - 1):
        n1 = x[i]
        n2 = x[i + 1]
        suc = False
        for j in range(len(l1)):
          if l1[j] == n1 and l2[j] == n2:
            suc = True
            break
        if suc == False:
          bigsuc = False
          break
      if bigsuc == False:
        i = 0
        while i < len(x) - 1:
          n1 = x[i]
          n2 = x[i + 1]
          suc = False
          for j in range(len(l1)):
            if l1[j] == n1 and l2[j] == n2:
              suc = True
              break
          if suc == False:
            x[i], x[i + 1] = x[i + 1], x[i]
            i = 0
            continue
          i += 1
        sum += x[len(x) // 2]
print(sum)

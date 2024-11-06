sum = 0
copies = { 1: 1 }
with open('./2023/test.txt', 'r') as file:
  for line in file:
    i = 0
    cardnum = 0
    dict = []
    matches = 0
    count = line.split()
    n = count.index('|')
    cardnum = (int)(count[1][:len(count[1]) - 1])
    while i < len(line):
      if line[i] == ':':
        i += 1
        numbers = line.split()
        dictInput = numbers[2:n]
        for num in dictInput:
          dict.append(num)
        dictTest = numbers[n + 1:]
        for num in dictTest:
          if dict.count(num) > 0:
            matches += 1
      i += 1
    multiplier = -1
    if cardnum == 17:
      print("a")
    if cardnum in copies:
      multiplier = copies[cardnum]
    else:
      copies[cardnum] = 1
      multiplier = 1
    temp = cardnum + 1
    while matches > 0:
      if temp in copies:
        copies[temp] += multiplier
      else:
        copies[temp] = 1 + multiplier
      temp += 1
      matches -= 1
for num in copies:
  sum += copies[num]
print(sum)
sum = 0
with open('./2023/input4.txt', 'r') as file:
  for line in file:
    i = 0
    dict = []
    points = 0
    count = line.split()
    n = count.index('|')
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
            if points == 0:
              points = 1
            else:
              points *= 2
      i += 1
    sum += points
print(sum)
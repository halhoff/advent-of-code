seeds = []
repeat = []
with open("./2023/input5.txt", 'r') as file:
  lines = file.readlines()
  lines[0] = lines[0][6:]
  seeds = list(map(int, lines[0].split()))
  mat = []
  n = 0
  lines.pop(0)
  for index, line in enumerate(lines):
    if line == '\n' and n == 0:
      n += 1
      continue
    elif (line == '\n' and n == 1) or index == len(lines) - 1:
      repeat = [False] * len(seeds)
      for i in range(len(mat)):
        destination = mat[i][0]
        source = mat[i][1]
        length = mat[i][2]
        for j in range(len(seeds)):
          if source <= seeds[j] <= source + length - 1 and repeat[j] == False:
            seeds[j] = seeds[j] - source + destination
            repeat[j] = True
      repeat.clear()
      mat.clear()
      continue
    if all(num.isdigit() for num in line.split()):
      mat.append(list(map(int, line.split())))
print(min(seeds))
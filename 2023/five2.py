seeds = []
ranges = []
with open("./2023/input5.txt", 'r') as file:
  lines = file.readlines()
  lines[0] = lines[0][6:]
  seeds = list(map(int, lines[0].split()))
  for i, seed in enumerate(seeds):
    if i % 2 == 1:
      ranges.append([seeds[i - 1], seeds[i - 1] + seeds[i] - 1])
  mat = []
  n = 0
  lines.pop(0)
  for index, line in enumerate(lines):
    if line == '\n' and n == 0:
      n += 1
      continue
    if line != '\n' and all(num.isdigit() for num in line.split()):
      mat.append(list(map(int, line.split())))
    if (line == '\n' and n == 1) or index == len(lines) - 1:
      new_ranges = []
      for i in range(len(mat)):
        destination = mat[i][0]
        source = mat[i][1]
        length = mat[i][2]
        start = source
        end = source + length - 1
        j = 0
        while j < len(ranges):
          if ranges[j][0] == start and end == ranges[j][1]:
            new_ranges.append([destination, destination + length - 1])
            ranges.pop(j)
          elif ranges[j][0] == start and end < ranges[j][1]:
            ranges[j] = [end + 1, ranges[j][1]]
            j -= 1
            new_ranges.append([destination, destination + length - 1])
          elif ranges[j][0] < start and end == ranges[j][1]:
            ranges[j] = [ranges[j][0], start - 1]
            j -= 1
            new_ranges.append([destination, destination + length - 1])
          elif ranges[j][0] < start and end < ranges[j][1]:
            ranges.append([ranges[j][0], start - 1])
            ranges[j] = [end + 1, ranges[j][1]]
            j -= 1
            new_ranges.append([destination, destination + length - 1])
          elif start <= ranges[j][0] and ranges[j][1] <= end: # [10, 20] [1, 30]
            new_ranges.append([ranges[j][0] - start + destination, ranges[j][1] - start + destination])
            ranges.pop(j)
            j -= 1
          elif start <= ranges[j][0] and end <= ranges[j][1] and start <= ranges[j][0] <= end:
            new_ranges.append([ranges[j][0] - start + destination, destination + length - 1])
            ranges[j] = [end + 1, ranges[j][1]]
            j -= 1
          elif ranges[j][0] <= start and ranges[j][1] <= end and ranges[j][0] <= start <= ranges[j][1]:
            new_ranges.append([destination, ranges[j][1] - start + destination])
            ranges[j] = [ranges[j][0], start - 1]
            j -= 1
          j += 1
      ranges += new_ranges
      mat.clear()
      continue
min_location = ranges[0][0]
for i in range(len(ranges)):
  min_location = min(min_location, ranges[i][0])
print(min_location)
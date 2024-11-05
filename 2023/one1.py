sum = 0
with open("test.txt", 'r') as file:
  for line in file:
    temp = 0
    for i in range(len(line)):
      if '0' <= line[i] <= '9':
        temp += 10 * (int)(line[i])
        break
    for i in range(len(line)):
      if '0' <= line[len(line) - i - 1] <= '9':
        temp += (int)(line[len(line) - i - 1])
        break
    sum += temp
print(sum)
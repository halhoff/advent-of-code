sum = 0
dict = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
}
with open("input.txt", 'r') as file:
  for line in file:
    firstDigit = -1
    lastDigit = -1
    for i in range(len(line)):
      if '0' <= line[i] <= '9':
        if firstDigit == -1:
          firstDigit = (int)(line[i])
        lastDigit = (int)(line[i])
        continue
      for num in dict:
        for j in range(2,6):
          yuh = line[i:i + j + 1]
          if i < len(line) - j and line[i:i + j + 1] == num:
            if firstDigit == -1:
              firstDigit = dict[num]
            lastDigit = dict[num]
    sum += 10 * firstDigit + lastDigit
print(sum)
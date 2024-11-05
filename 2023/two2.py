sum = 0
with open("input2.txt", 'r') as file:
  for line in file:
    invalid = False
    words = line.split()
    id = words[1][:len(words[1]) - 1]
    count = 1
    num = ""
    color = ""
    minRed = -1
    minGreen = -1
    minBlue = -1
    for word in words[2:]:
      if count % 2 == 1:
        num = word
      else:
        color = word
        if color[len(color) - 1] == ',' or color[len(color) - 1] == ';':
          color = color[:len(color) - 1]
        if color == "red":
          minRed = max((int)(num), minRed)
        elif color == "green":
          minGreen = max((int)(num), minGreen)
        elif color == "blue":
          minBlue = max((int)(num), minBlue)
      count += 1
    sum += minRed * minGreen * minBlue
print(sum)
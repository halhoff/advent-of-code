sum = 0
with open("input2.txt", 'r') as file:
  for line in file:
    invalid = False
    words = line.split()
    id = words[1][:len(words[1]) - 1]
    count = 1
    num = ""
    color = ""
    for word in words[2:]:
      if count % 2 == 1:
        num = word
      else:
        color = word
        if color[len(color) - 1] == ',' or color[len(color) - 1] == ';':
          color = color[:len(color) - 1]
        if color == "red":
          if (int)(num) > 12:
            invalid = True
            break
        elif color == "green":
          if (int)(num) > 13:
            invalid = True
            break
        elif color == "blue":
          if (int)(num) > 14:
            invalid = True
            break
      count += 1
    if not invalid:
      sum += (int)(id)
print(sum)
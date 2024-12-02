safe = 0
with open("./2024/input2.txt", 'r') as file:
  for line in file:
    l = [int(x) for x in line.split()]
    for k in range(len(l)):
      lll = l.copy()
      lll.pop(k)
      ll = lll
      i = ll[0]
      increasing = False
      toggle = False
      unsafe = False
      for j in range(1, len(ll)):
        if ll[j] == i:
          unsafe = True
          break
        elif abs(i - ll[j]) > 3:
          unsafe = True
          break
        elif ll[j] > i and not toggle:
          increasing = True
          toggle = True
          i = ll[j]
          continue
        elif ll[j] < i and not toggle:
          increasing = False
          toggle = True
          i = ll[j]
          continue
        elif ll[j] < i and increasing and toggle:
          unsafe = True
          break
        elif ll[j] > i and not increasing and toggle:
          unsafe = True
          break
        i = ll[j]
      if not unsafe:
        safe += 1
        break
print(safe)
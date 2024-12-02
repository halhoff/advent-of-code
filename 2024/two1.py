safe = 0
with open("./2024/input2.txt", 'r') as file:
  for line in file:
    l = [int(x) for x in line.split()]
    i = l[0]
    increasing = False
    toggle = False
    unsafe = False
    for j in range(1, len(l)):
      if l[j] == i:
        unsafe = True
        break
      elif abs(i - l[j]) > 3:
        unsafe = True
        break
      elif l[j] > i and not toggle:
        increasing = True
        toggle = True
        i = l[j]
        continue
      elif l[j] < i and not toggle:
        increasing = False
        toggle = True
        i = l[j]
        continue
      elif l[j] < i and increasing and toggle:
        unsafe = True
        break
      elif l[j] > i and not increasing and toggle:
        unsafe = True
        break
      i = l[j]
    if not unsafe:
      safe += 1
print(safe)
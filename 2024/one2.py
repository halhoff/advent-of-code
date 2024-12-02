l1 = []
l2 = {}
with open("./2024/input1.txt", 'r') as file:
  for line in file:
    a = line.split()
    l1.append(int(a[0]))
    if int(a[1]) not in l2:
      l2[int(a[1])] = 1
    else:
      l2[int(a[1])] += 1
sum = 0
for i in range(len(l1)):
  if l1[i] in l2:
    sum += l1[i] * l2[l1[i]]
print(sum)

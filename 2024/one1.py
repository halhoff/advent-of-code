l1 = []
l2 = []
with open("./2024/input1.txt", 'r') as file:
  for line in file:
    a = line.split()
    l1.append(int(a[0]))
    l2.append(int(a[1]))
l1.sort()
l2.sort()
sum = 0
for i in range(len(l1)):
  sum += abs(l2[i] - l1[i])
print(sum)
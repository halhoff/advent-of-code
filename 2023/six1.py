# record if > distance
# distance = button * (time - button)
time = []
distance = []
ways = 1
with open("./2023/input6.txt", 'r') as file:
  for line_num, line in enumerate(file):
    if line_num == 0:
      time = line.split()
      time = time[1:]
      time = [int(x) for x in time]
    else:
      distance = line.split()
      distance = distance[1:]
      distance = [int(x) for x in distance]
  for i in range(len(time)):
    current_time = time[i]
    current_distance = distance[i]
    temp = 0
    for j in range(1, current_time):
      calculated_distance = j * (current_time - j)
      if calculated_distance > current_distance:
        temp += 1
    ways *= temp
print(ways)
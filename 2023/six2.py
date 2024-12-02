time = 0
distance = 0
ways = 1
with open("./2023/input6.txt", 'r') as file:
  for line_num, line in enumerate(file):
    if line_num == 0:
      time_arr = line.split()
      time_arr = time_arr[1:]
      time_str = ""
      for i in time_arr:
        time_str += i
      time = int(time_str)
    else:
      distance_arr = line.split()
      distance_arr = distance_arr[1:]
      distance_str = ""
      for i in distance_arr:
        distance_str += i
      distance = int(distance_str)
  temp = 0
  for i in range(1, time):
      calculated_distance = i * (time - i)
      if calculated_distance > distance:
        temp += 1
  ways *= temp
print(ways)
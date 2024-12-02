with open("./2023/input7.txt", 'r') as file:
  for lines in file:
    card_to_value = {
      'A': 14,
      'K': 13,
      'Q': 12,
      'J': 11,
      'T': 10
    }
    line = lines.split()
    card = line[0]
    bid = line[1]
    rank = 0
    dict = {}
    for i in range(len(card)):
      if dict[card[i]]:
        dict[card[i]] += 1
      else:
        dict[card[i]] = 1
    nums = []
    for key in dict.keys:
      nums.append(dict[key])
    nums.sort()
    if nums == [5]:
      rank = 7
    elif nums == [1, 4]:
      rank = 6
    elif nums == [2, 3]:
      rank = 5
    elif nums == [1, 1, 3]:
      rank = 4
    elif nums == [1, 2, 2]:
      rank = 3
    elif nums == [1, 1, 1, 2]:
      rank = 2
    elif nums == [1, 1, 1, 1, 1]:
      rank = 1
    score = rank * 100000
    for i in range(len(card)):
      value = 0
      if card[i] in card_to_value.keys:
        value = card_to_value[card[i]] 
      else:
        value = int(card[i])
      score += value * (4 - i)
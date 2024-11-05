sum = 0
mat = []
with open("input3.txt", 'r') as file:
  for line in file:
    mat.append(line)
for index, line in enumerate(mat):
  i = 0
  line = line[:len(line) - 1]
  while i < len(line):
    if line[i] == '*':
      used = []
      first = -1
      second = -1
      if i > 0 and '0' <= line[i - 1] <= '9':
        j = i - 1
        while '0' <= line[j - 1] <= '9':
          j -= 1
        if first > 0:
          second = (int)(line[j:i])
          sum += first * second
          i += 1
          continue
        else:
          first = (int)(line[j:i])
      if i < len(line) - 1 and '0' <= line[i + 1] <= '9':
        j = i + 1
        while '0' <= line[j + 1] <= '9':
          j += 1
        if first > 0:
          second = (int)(line[i + 1:j + 1])
          sum += first * second
          i += 1
          continue
        else:
          first = (int)(line[i + 1:j + 1])
      if index != len(mat) - 1:
        if i > 0 and '0' <= mat[index + 1][i - 1] <= '9':
          used.append(6)
          j = i - 1
          k = i - 1
          while '0' <= mat[index + 1][j + 1] <= '9':
            j += 1
            if j - i + 7 < 9:
              used.append(j - i + 7)
          while '0' <= mat[index + 1][k - 1] <= '9':
            k -= 1
          if first > 0:
            second = (int)(mat[index + 1][k:j + 1])
            sum += first * second
            i += 1
            continue
          else:
            first = (int)(mat[index + 1][k:j + 1])
        elif '0' <= mat[index + 1][i] <= '9':
          used.append(7)
          j = i
          k = i
          while '0' <= mat[index + 1][j + 1] <= '9':
            j += 1
            if j - i + 7 < 9:
              used.append(j - i + 7)
          while '0' <= mat[index + 1][k - 1] <= '9':
            k -= 1
          if first > 0:
            second = (int)(mat[index + 1][k:j + 1])
            sum += first * second
            i += 1
            continue
          else:
            first = (int)(mat[index + 1][k:j + 1])
        if i < len(line) - 1 and '0' <= mat[index + 1][i + 1] <= '9':
          j = i + 1
          k = i + 1
          while '0' <= mat[index + 1][j + 1] <= '9':
            j += 1
          while '0' <= mat[index + 1][k - 1] <= '9':
            k -= 1
          if first > 0 and used.count(8) == 0:
            second = (int)(mat[index + 1][k:j + 1])
            sum += first * second
            i += 1
            continue
          else:
            first = (int)(mat[index + 1][k:j + 1])
      if index != 0:
        if i > 0 and '0' <= mat[index - 1][i - 1] <= '9':
          used.append(1)
          j = i - 1
          k = i - 1
          while '0' <= mat[index - 1][j + 1] <= '9':
            j += 1
            if j - i + 2 < 4:
              used.append(j - i + 2)
          while '0' <= mat[index - 1][k - 1] <= '9':
            k -= 1
          if first > 0:
            second = (int)(mat[index - 1][k:j + 1])
            sum += first * second
            i += 1
            continue
          else:
            first = (int)(mat[index - 1][k:j + 1])
        elif '0' <= mat[index - 1][i] <= '9':
          used.append(2)
          j = i
          k = i
          while '0' <= mat[index - 1][j + 1] <= '9':
            j += 1
            if j - i + 2 < 4:
              used.append(j - i + 2)
          while '0' <= mat[index - 1][k - 1] <= '9':
            k -= 1
          if first > 0:
            second = (int)(mat[index - 1][k:j + 1])
            sum += first * second
            i += 1
            continue
          else:
            first = (int)(mat[index - 1][k:j + 1])
        if i < len(line) - 1 and '0' <= mat[index - 1][i + 1] <= '9':
          j = i + 1
          k = i + 1
          while '0' <= mat[index - 1][j + 1] <= '9':
            j += 1
          while '0' <= mat[index - 1][k - 1] <= '9':
            k -= 1
          if first > 0 and used.count(3) == 0:
            second = (int)(mat[index - 1][k:j + 1])
            sum += first * second
            i += 1
            continue
          else:
            first = (int)(mat[index - 1][k:j + 1])
    i += 1
print(sum)
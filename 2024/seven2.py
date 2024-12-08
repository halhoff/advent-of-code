def f(n: list[int], o: list[int]) -> list[int]:
  if len(n) == 1:
    return [n[0]]
  l = f(n[:len(n) - 1], [])
  p = [x + n[len(n) - 1] for x in l]
  q = [x * n[len(n) - 1] for x in l]
  r = [int(str(x) + str(n[len(n) - 1])) for x in l]
  o.extend(p)
  o.extend(q)
  o.extend(r)
  return o
a = [l.strip() for l in open("./2024/input7.txt")]
s = 0
for n in a:
  p = [x for x in n.split()]
  t = int(p[0][:len(p[0]) - 1])
  p.pop(0)
  p = [int(x) for x in p]
  if t in f(p, []):
    s += t
print(s)
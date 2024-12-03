f = open("input.txt", 'r')
lines = f.read().splitlines()

l1, l2 = [], []

for line in lines:
  s = [int(x) for x in line.split("   ")]
  l1.append(s[0])
  l2.append(s[1])


### Part I
_l1 = sorted(l1)
_l2 = sorted(l2)
dis = 0

for i in range(len(_l1)):
  dis += abs(_l1[i] - _l2[i])

print(s)


### Part II
sim = 0

for i in range(len(l1)):
  sim += l1[i] * l2.count(l1[i])

print(sim)

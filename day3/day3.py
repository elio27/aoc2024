import re


def prod(mul):
  x = [int(_) for _ in mul[4:-1].split(",")]
  return x[0]*x[1]

f = open("input.txt", 'r')
text = f.read()

### Part I
matches = re.findall("mul\(\d{1,3},\d{1,3}\)", text)
s = 0
for mul in matches:
  s += prod(mul)

print(s)


### Part II
matches = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", text)
s = 0
enabled = True
for m in matches:
  if m == "do()":
    enabled = True
  elif m == "don't()":
    enabled = False
  elif enabled:
    s += prod(m)

print(s)

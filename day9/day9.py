def load_map(filepath):
  with open(filepath, 'r') as f:
    data = f.read().replace("\n","")
  id = 0
  map = []
  for i in range(len(data)):
    if i%2:
      map.append(["."]*int(data[i]))
    else:
      map.append([str(id)]*int(data[i]))
      id +=1
  return map


def unpack(grid):
  newgrid = []
  for bl in grid:
    for e in bl:
      newgrid.append(e)
  return newgrid


def fill_block(free, data):
  u0 = free.index(".")
  newblock = free
  for i in range(len(data)):
    newblock[u0 + i] = data[i]
  return newblock


def free_space(block):
  return block.count(".")



## Part I
grid = unpack(load_map("input 3.txt"))
while grid[-1]==".": grid.pop()
free = [i for i, c in enumerate(grid) if c=="."]
for f in free:
  while grid[-1]==".": grid.pop()
  if "." in grid:
    grid[f] = grid.pop()
  else:
    break

s = 0
for i in range(len(grid)):
  s += int(grid[i])*i
print(s)



## Part II
grid = load_map("input 3.txt")
for ni in range(0, len(grid), 2)[::-1]:
  n = grid[ni]
  for bi in range(1, ni, 2):
    b = grid[bi]
    if free_space(b) >= len(n):
      grid[bi] = fill_block(b, n)
      grid[ni] = ["."]*len(n)
      break

grid = unpack(grid)
s = 0
for i in range(len(grid)):
  if grid[i] != '.':
    s += int(grid[i])*i
print(s)


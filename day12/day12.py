def load_map(filepath):
  with open(filepath, 'r') as f:
    data = f.read()
  return [list(line)for line in data.splitlines()]


def get_adj(grid, x, y):
  dep = [[-1, 0],[0, -1],[0, 1],[1, 0]]
  t = grid[x][y]
  adj=[]
  for dx,dy in dep:
    if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[x]):
      if grid[x+dx][y+dy]==t:
        adj.append([x+dx, y+dy])
  return adj



grid = load_map("input.txt")
seen = []
zones = []
for i in range(len(grid)):
  for j in range(len(grid[i])):
    p = [i, j]
    if not p in seen:
      z = [p]
      rem = get_adj(grid, i, j)
      seen.append(p)
      while len(rem):
        for p1 in rem:
          if not p1 in seen:
            seen.append(p1)
            z.append(p1)
            rem.remove(p1)
            adj = get_adj(grid, p1[0], p1[1])
            for a in adj:
              if a not in seen and a not in rem:
                rem.append(a)
      zones.append(z)

## Part I
tot = 0
for zone in zones:
  a = len(zone)
  p = 0
  for x in zone:
    p += 4-len(get_adj(grid, x[0], x[1]))
  tot += a*p

print(tot)


## Part II
tot = 0
for z in zones:
  a = len(z)
  sides = 0
  for pos in z:
    x, y = pos[0], pos[1]
    if [x+1, y] in z:
          sides += int([x+1, y-1] in z and not [x, y-1] in z) + int([x+1, y+1] in z and not [x, y+1] in z)
    else:
      sides += int(not [x, y-1] in z) + int(not [x, y+1] in z)
  tot += 2*sides*a

print(tot)
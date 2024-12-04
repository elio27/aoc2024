re.findall("mul\(\d{1,3},\d{1,3}\)", text)

## Part I
def count_xmas(data):
  row, cols = len(data), len(data[0])
  d = [
    [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]
  ]

def isvalid(x, y):
  return x >= 0 and rows > x and y >= 0 and y <= cols

def check(xi, yi, dx, dy):
  for i in range(4):
    xx = xi + i*dx
    yy = yi + i*dy
    if not isvalid(xx,yy) or data[xx][yy]!="XMAS"[i]:  return False
  return True

count = 0
for row in range(rows):
  for col in range(cols):
    for di in d:
      count += int(check(row, col, di[0], di[1])

return count


## Part II
def count_xxmas(data):
  rows, cols = len(data), len(data[0])
  xstrings = ["MAS", "SAM"]

  def isvalid(x,y):
    return x - 1 >= 0 and x + 1 < rows and y - 1 >= 0 and y+1 < cols
  
  def check(xi, yi):
    for s1 in xstrings:
      for s2 in xstrings:
        if (
          isvalid(xi, yi) and
          data[xi - 1][yi - 1] == s1[0] and data[xi][yi] == s1[1] and data[xi + 1][yi + 1] == s1[2] and
          data[xi - 1][yi + 1] == s2[0] and data[xi + 1][yi - 1] == s2[2]
        ):
          return True
  return False

count = 0
for row in range(1, rows-1):
  for col in range(1, cols-1):
    count += int(check(row, col))
    
return count



## Get results
print(count_xmas(data))
print(count_xxmas(data))

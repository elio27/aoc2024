def load_map(filepath):
    with open(filepath, 'r') as f:
        grid = [list(line) for line in f.read().splitlines()]
    antennas = {}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != ".":
                if not grid[r][c] in antennas.keys():
                    antennas[grid[r][c]] = [[r, c]]
                else:
                    antennas[grid[r][c]] += [[r, c]]
    return grid, antennas

## Part I
def find_antinodes1(grid, antennas):
    rows,cols = len(grid), len(grid[0])
    antinodes = []
    for freq in antennas.values():
        for (x1, y1) in freq:
            for (x2, y2) in freq:
                dx, dy = x2-x1, y2-y1
                ax, ay = x2+dx, y2+dy
                if 0<=ax<rows and 0<=ay<cols and [ax,ay] not in antinodes and [dx,dy]!=[0,0]:
                    antinodes.append([ax, ay])
    return antinodes


## Part II
def find_antinodes2(grid, antennas):
    rows,cols = len(grid), len(grid[0])
    antinodes = []
    for freq in antennas.values():
        for (x1, y1) in freq:
            for (x2, y2) in freq:
                dx, dy = x2-x1, y2-y1
                ax, ay = x2+dx, y2+dy
                while 0<=ax<rows and 0<=ay<cols:
                    if [ax,ay] not in antinodes:
                        antinodes.append([ax, ay])
                    ax += dx
                    ay += dy
                    if dx==0 and dy==0: break
    return antinodes


grid, antennas = load_map("input.txt")
antinodes1 = find_antinodes1(grid, antennas)
antinodes2 = find_antinodes2(grid, antennas)
#for x,y in antinodes1:                          # Map viewer
#    grid[x][y] = "#"
#print("\n".join("".join(line)for line in grid))
print(len(antinodes1))
print(len(antinodes2))
                
            

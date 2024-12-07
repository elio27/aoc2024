class Patrol:
    def __init__(self, data):
        self.data = data
        self.map = [list(line) for line in data.splitlines()]
        self.x, self.y = None, None
        self.dx, self.dy = None, None
        self.path = None
        
    def find_guardian(self):
        match = {">":(0,1), "<":(0,-1), "^":(-1, 0), "v":(1, 0)}
        for line in self.map:
            for k in match.keys():
                if k in line:
                    self.x, self.y = self.map.index(line), line.index(k)
                    self.dx, self.dy = match[k]
                    self.map[self.x][self.y] = "."
                    return
                    
    def turn_right(self):
        self.dx, self.dy = self.dy, -self.dx
        
    def forward(self):
        self.x, self.y = self.x+self.dx, self.y+self.dy
    
    def peek(self):
        if 0 <= self.x + self.dx < len(self.map) and 0 <= self.y + self.dy < len(self.map[self.x]):
            return self.map[self.x + self.dx][self.y + self.dy]
        else:
            return 0
            
    def patrol(self):
        self.find_guardian()
        visited = [[self.x, self.y]]
        while True:
            p = self.peek()
            if p == ".":
                self.forward()
                if not [self.x, self.y] in visited:
                    visited.append([self.x, self.y])
            elif p == "#":
                self.turn_right()
            else:
                break
            
        self.path = visited
        return len(visited)
        
        
    def patrol2(self):
        obcount = 0
        for r,c in self.path:
            self.map = [list(line) for line in self.data.splitlines()]
            self.map[r][c] = "#"
            self.find_guardian()
            visited = [[self.x, self.y, self.dx, self.dy]]
            while True:
                p = self.peek()
                if p == "#" :
                    self.turn_right()
                elif p == ".":
                    self.forward()
                    if not [self.x, self.y, self.dx, self.dy] in visited:
                        visited.append([self.x, self.y, self.dx, self.dy])
                    else:
                        obcount += 1
                        break
                else:
                    break
        return obcount
        
    
with open("input.txt", 'r') as f:
    data = f.read()
  
pat = Patrol(data)
print(pat.patrol())
print(pat.patrol2())

f = open("input.txt", 'r')
lines = f.read().spltlines()

def treated(line):
  return [int(n) for n in line.split()]
	

def isSafe(treatedline):
	d = treatedline[1] - treatedline[0]
	last = treatedline[0]
	
  for e in treatedline[1:]:
    if (d>0 and e > last or d<0 and e < last) and abs(e - last) <= 3:
      last = e
    else:
      return False
	return True


### Part I
tot = 0
for l in lines:
	tot += int(isSafe(treated(l)))
print(tot)


### Part II
tot = 0
for l in lines:
	line = treated(l)
	safe = isSafe(line)
  
	for i in range(len(line)):
		safe = safe or isSafe( line[:i] + line[i+1:] )
	tot += int(safe)

print(tot)

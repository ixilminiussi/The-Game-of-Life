from operator import methodcaller
import numpy as np
import sys

g = []
G = {}

with open(sys.argv[2],'r') as f:
    lines = map(methodcaller('strip', '\n'), f.readlines())
    data = list(map(methodcaller('split', ','), lines))
    
    for i in range(len(data)): data[i] = list(map(int, data[i]))
        
    data.sort(key = lambda i: i[1])
    
    for i in data:
        if i[2] not in g: 
            g.append(i[2])
            G[i[2]] = []
            
        G[i[2]].append(i)

def generate_grid(i):
    data = sorted(G[i], key = lambda x: (-x[1], -x[0]))
    X = data[0][0] + 1
    Y = data[0][1] +1 
    
    grid = np.zeros((Y, X))
    
    for e in data:
        grid[e[1]][e[0]] = e[3]
    
    return grid
    
print(generate_grid(int(sys.argv[1])))

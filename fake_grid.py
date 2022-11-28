import random as rd

with open('output.txt', 'w') as f:
    for g in reversed(range(0,10)):
        for y in reversed(range(0,40)):
            for x in reversed(range(0,30)):
                f.write('%d, %d, %d, %d\n' % (x, y, g, rd.randint(0,1)))

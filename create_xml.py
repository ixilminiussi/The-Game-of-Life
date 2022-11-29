from operator import methodcaller
import sys

device_instances = '<DeviceInstances>\n'
edge_instances = '<EdgeInstances>\n'

input_f = sys.argv[1]
output_f = sys.argv[2]

with open(input_f,'r') as f:    
    lines = map(methodcaller('strip', '\n'), f.readlines())
    data = list(map(methodcaller('split', ','), lines))
    
Y = len(data)
X = len(data[0])

id = 0

##############
##NEIGHBOURS##
##############

def right(id):
    if (id +1) % X == 0:
        return id - X +1
    return id +1
    
def left(id):
    if id % X == 0:
        return id + X -1
    return id -1

def top(id):
    if id < X:
        return id + X * (Y -1)
    return id - X

def bottom(id):
    if id >= X * (Y -1):
        return id % X
    return id + X

def top_right(id):
    return top(right(id))

def top_left(id):
    return top(left(id))
    
def bottom_right(id):
    return bottom(right(id))

def bottom_left(id):
    return bottom(left(id))

###########
##WRITING##
###########

for y in range(Y):
    for x in range(X):
        device_instances += '<DevI id="%d" type="cell" P="{%s,%d,%d}" />\n' % (id,data[y][x],x,y)
        
        edge_instances += '<EdgeI path="%d:receiver-%d:sender" />\n' % (id,top_left(id))
        edge_instances += '<EdgeI path="%d:receiver-%d:sender" />\n' % (id,top(id))
        edge_instances += '<EdgeI path="%d:receiver-%d:sender" />\n' % (id,top_right(id))
        edge_instances += '<EdgeI path="%d:receiver-%d:sender" />\n' % (id,right(id))
        edge_instances += '<EdgeI path="%d:receiver-%d:sender" />\n' % (id,bottom_right(id))
        edge_instances += '<EdgeI path="%d:receiver-%d:sender" />\n' % (id,bottom(id))
        edge_instances += '<EdgeI path="%d:receiver-%d:sender" />\n' % (id,bottom_left(id))
        edge_instances += '<EdgeI path="%d:receiver-%d:sender" />\n' % (id,left(id))
        
        id += 1

device_instances += "</DeviceInstances>"
edge_instances += "</EdgeInstances>"

xml_graph = device_instances + "\n\n" + edge_instances

with open(output_f, 'w') as f:
    f.write(xml_graph)

print('graph written to %s succesfully' % output_f)

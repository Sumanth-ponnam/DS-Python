#pip3 install criticalpath
from criticalpath import Node
p = Node('project')
a = p.add(Node('A', duration=3))
b = p.add(Node('B', duration=3))
c = p.add(Node('C', duration=4))
d = p.add(Node('D', duration=6))
e = p.add(Node('E', duration=5))
p.link(a, b).link(a, c).link(a, d).link(b, e).link(c, e).link(d, e)
p.update_all()
print('Critical path duration is:',p.duration)
